import click

from yakyuken.comands import generate_command, jsonToBytes_command


@click.group()
def cli():
    """
    Mezzanotte Yakyuken Generator

    The command line generator for Yakyuken NFTs.
    """
    pass


cli.add_command(generate_command)
cli.add_command(jsonToBytes_command)
