import click

from yakyuken.comands import generate_command, jsonToBytes_command, regenerate_command


@click.group()
def cli():
    """
    Mezzanotte Yakyuken Generator

    The command line generator for Yakyuken NFTs.
    """
    pass


cli.add_command(generate_command)
cli.add_command(jsonToBytes_command)
cli.add_command(regenerate_command)
