import os
import random

import click
import tqdm
import json

from yakyuken.core import convert_json_to_bytes


@click.command("jsonToBytes")
@click.option(
    "--json_file", default=0, show_default=True, help="TokenId of the jsonFile to generate to bytes"
)
@click.option(
    "--all_files", default=False, show_default=True, help="True to convert all the json files from the out folder."
)
@click.option(
    "--out",
    type=click.Path(file_okay=True),
    default="out/byteRepresentation.json",
    show_default=True,
    help="Output directory.",
)
def jsonToBytes_command(json_file: int, all_files:bool, out: click.Path) -> None:
    if os.path.exists(out):
        os.remove(out)
    jsonToDump = {}
    if all_files == True:
        # List all files in the folder
        files = os.listdir("out/")

        # Filter for .json files
        json_files_list = [file for file in files if (file.endswith(".json") and "byte" not in file )]
        json_files_list = sorted(json_files_list)
        for file in json_files_list:
            (tokenId, byteRepresentation) = convert_json_to_bytes("out/" + file)
            jsonToDump[tokenId] = byteRepresentation
        with open(out, "a") as file:
            json.dump(jsonToDump, file, indent=4)
    else:
        file_name = "out/" + str(json_file) + ".json"
        (tokenId, byteRepresentation) = convert_json_to_bytes(file_name)
        jsonToDump = {tokenId: byteRepresentation}
        with open(out, "a") as file:
            json.dump(jsonToDump, file, indent=4)