import rich_click as click
from .build import build


@click.group()
def cli():
    pass


def main():
    cli()


@cli.command("build")
def buildcli():
    build()


if __name__ == "__main__":
    main()
