import click

from yakyuken.comands import generate_command


@click.group()
def cli():
    """
    Mezzanotte Yakyuken Generator

    The command line generator for Yakyuken NFTs.
    """
    pass


cli.add_command(generate_command)
