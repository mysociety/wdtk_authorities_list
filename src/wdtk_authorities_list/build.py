from re import X
import pandas as pd
from pathlib import Path
import urllib.request
from urllib.error import HTTPError
from rich import print
from bs4 import BeautifulSoup, Tag

top_level = Path(__file__).parent.parent.parent


def series_to_ordered_pipe(s: pd.Series | list) -> str:

    if isinstance(s, pd.Series):
        return "|".join(s.sort_values())
    else:
        return "|".join(sorted(s))


def safe_url(url: str) -> str:
    """
    check each character is able to be in a valid url and remove the character if not
    """
    safe_url = ""
    for char in url:
        if char.isalnum() or char in [
            "-",
            "_",
            ".",
            "~",
            "*",
            "'",
            "(",
            ")",
            ":",
            ";",
            "&",
            "=",
            "+",
            "%",
            ",",
            "?",
            "!",
            "@",
            "#",
            "$",
            "`",
            "[",
            "]",
        ]:
            safe_url += char
    return safe_url


def retrieve_tags():
    """
    Download the WDTK authorities list and parse the relevant tags for the Authority categories from the URLs.
    """
    print("[blue]Retrieving tags from authorities list...[/blue]")
    url = "https://www.whatdotheyknow.com/body/list/all"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    sidebar = soup.find("div", {"id": "right_column_flip"})
    if not isinstance(sidebar, Tag):
        raise ValueError("Could not find the sidebar on the WDTK page.")
    # iterate through all subelements of the sidebar

    # populate a list of top-level category, category name, and category tag
    # e.g. ["Central government", "Ministerial departments", "department"]
    # these are stored as a list of elements in the html
    # there is a h3 tag for the top-level category, followed by a ul that contains list items
    # with categories names, and links to the category pages. The last element of the url is the category tab.

    # iterate through the sidebar elements and create this list

    top_level_category = ""
    all_categories = []
    for element in sidebar.find_all():
        # if the element is a h3 tag, it is the top-level category
        if element.name == "h3":
            top_level_category = element.text
            # print(top_level_category)
        # if the element is a ul tag, it is the list of categories
        if element.name == "ul":
            for li in element.find_all("li"):
                # get the category name
                category_name = li.text.strip()
                # get the category tag
                category_tag = li.find("a")["href"].split("/")[-1]
                # print(category_name, category_tag)
                # create a list of the three elements
                category_list = [top_level_category, category_name, category_tag]
                # append the list to the list of all categories
                # if the current top_level_category is "Beginning with", skip
                if top_level_category == "Beginning with":
                    continue
                all_categories.append(category_list)

    # create a dataframe from the list of all categories
    df = pd.DataFrame(
        all_categories, columns=["top-level-category", "category-name", "category-tag"]
    )

    # it is possible for a tag to be in multiple top_level categories
    df = (
        df.groupby(["category-tag"])
        .agg(
            {
                "top-level-category": series_to_ordered_pipe,
                "category-name": "first",
            }
        )
        .reset_index()
    )

    df.to_csv(top_level / "data" / "raw" / "authorities_categories.csv", index=False)
    df.to_csv(
        top_level
        / "data"
        / "packages"
        / "whatdotheyknow_authorities_dataset"
        / "authorities_categories.csv",
        index=False,
    )
    print("[green]Saved authorities categories list.[/green]")


def download_authorities_csv():
    """
    Download the authorities list from the WDK and save it to a CSV file.
    This file takes a little time to generate and needs a long timeout.
    """
    print("[blue]Downloading authorities list...[/blue]")
    file_url = "https://www.whatdotheyknow.com/body/all-authorities.csv"
    file_path = top_level / "data" / "raw" / "authorities.csv"
    file_downloaded = False
    retry_attempts = 0
    while file_downloaded is False and retry_attempts < 5:
        try:
            request = urllib.request.urlopen(file_url, timeout=120)
            with open(file_path, "wb") as f:
                f.write(request.read())
            file_downloaded = True
        except HTTPError as e:
            retry_attempts += 1
            print("[red]Retrying download...[/red]")
            if retry_attempts == 6:
                raise (e)
            else:
                continue
    if file_downloaded:
        print("[green]Downloaded authorities list.[/green]")


def enhance_authorities_csv():
    """
    Reorder the csv and add columns for specific tags and categories.
    """

    print("[blue]Enhancing authorities list...[/blue]")
    # get the ID lookup - will be unneeded when PR is eventually merged
    id_df = pd.read_csv(top_level / "data" / "raw" / "id_to_name.csv")
    id_lookup = id_df.set_index("url_name")["id"].to_dict()

    # get the category df
    category_df = pd.read_csv(top_level / "data" / "raw" / "authorities_categories.csv")
    # create a dictionary lookup for tag to category name
    tag_to_category = category_df.set_index("category-tag")["category-name"].to_dict()
    # create a dictionary lookup for tag to top level category
    tag_to_top_level_category = category_df.set_index("category-tag")[
        "top-level-category"
    ].to_dict()

    df = pd.read_csv(top_level / "data" / "raw" / "authorities.csv")
    df = df.rename(columns=lambda x: x.lower().replace(" ", "-"))

    df["id"] = df["url-name"].apply(lambda x: id_lookup.get(x, "Unknown ID"))
    # move ID column to the front
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    df["tags"] = df["tags"].fillna("").str.split(" ")

    # create boolean columns from the presence of a tag
    boolean_columns = ["defunct"]
    for b in boolean_columns:
        df[b] = df.apply(lambda x: b in x["tags"], axis=1)

    def apply_and_reduce(tags: list[str], di: dict[str, str]):
        """
        Convert the tags through the dictionary and reduce
        categories may include pipe seperated values
        """
        categories = [di.get(t, None) for t in tags]
        categories = [x for x in categories if x is not None]
        categories = [c.split("|") for c in categories]
        categories = [item for sublist in categories for item in sublist]
        return list(set(categories))

    def get_highest_priority_option(categories: list[str]) -> str:
        """
        It is possible to have multiple top level categories, pick the one with the highest priority.
        """
        priority_order = [
            "Central government",
            "Devolved Administration",
            "Local and regional",
            "Law making bodies, the courts and the legal system",
            "Health",
            "Education",
            "Emergency services",
            "Transport and infrastructure",
            "Environment and agriculture",
            "Groups of public authorities",
            "Media and culture",
            "Recreation",
            "Military and security services",
            "Other",
            "Forthcoming",
            "Defunct bodies",
        ]

        for c in priority_order:
            if c in categories:
                return c
        return ""

    # create a column for the category
    df["categories"] = df["tags"].apply(lambda x: apply_and_reduce(x, tag_to_category))
    df["top-level-categories"] = df["tags"].apply(
        lambda x: apply_and_reduce(x, tag_to_top_level_category)
    )
    df["single-top-level-category"] = df["top-level-categories"].map(
        get_highest_priority_option
    )

    pipe_seperated_columns = [
        "tags",
        "categories",
        "top-level-categories",
    ]
    for c in pipe_seperated_columns:
        df[c] = df[c].apply(series_to_ordered_pipe)

    # fix url error that breaks excel
    df["home-page"] = df["home-page"].fillna("").apply(safe_url)

    df.to_csv(
        top_level
        / "data"
        / "packages"
        / "whatdotheyknow_authorities_dataset"
        / "authorities.csv",
        index=False,
    )

    print("[green]Saved authorities list.[/green]")


def create_id_lookup_from_tags():
    """
    Some tags are ID values in the format "schema:id"
    Create a new dataframe of "schema", "id", "wdtk-url-name" from the
    authorities table.
    """
    print("[blue]Creating id lookup from tags...[/blue]")
    df = pd.read_csv(top_level / "data" / "raw" / "authorities.csv")
    df = df.rename(columns=lambda x: x.lower().replace(" ", "-"))
    df["tags"] = df["tags"].fillna("").str.split(" ")
    df["ids"] = df["tags"].apply(lambda tags: [x for x in tags if ":" in x])

    # drop all rows without a value in ids
    df = df[df["ids"].apply(lambda x: len(x) > 0)]

    df = df.explode("ids")
    values = []
    for _, row in df.iterrows():
        schema, schema_id = row["ids"].split(":")
        values.append(
            {
                "schema": schema,
                "id": schema_id,
                "wdtk-url-name": row["url-name"],
            }
        )
    df = pd.DataFrame(values)
    df.to_csv(
        top_level
        / "data"
        / "packages"
        / "whatdotheyknow_authorities_dataset"
        / "authorities_id_lookup.csv",
        index=False,
    )
    print("[green]Saved authorities id lookup.[/green]")


def build():
    download_authorities_csv()
    retrieve_tags()
    enhance_authorities_csv()
    create_id_lookup_from_tags()


if __name__ == "__main__":
    build()
