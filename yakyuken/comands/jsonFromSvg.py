import os
import random

import click
import tqdm
import json

from yakyuken.core import convert_from_svg_to_json


@click.command("jsonFromSvg")
@click.option(
    "--json_file", default=0, show_default=True, help="TokenId of the jsonFile to generate to bytes"
)
@click.option(
    "--all_files", default=False, show_default=True, help="True to convert all the json files from the out folder."
)
@click.option(
    "--out",
    type=click.Path(file_okay=True),
    default="desired_out/",
    show_default=True,
    help="Output directory.",
)
def jsonFromSvg_command(json_file: int, all_files:bool, out: click.Path) -> None:
    if all_files == True:
        # List all files in the folder
        files = os.listdir(out)

        # Filter for .json files
        svg_files_list = [file for file in files if (file.endswith(".svg") )]
        svg_files_list = sorted(svg_files_list)
        for file_path in svg_files_list:
            file_name = out + file_path
            with open(file_name, 'r') as file:
                # Read the entire file into a string
                file_contents = file.read()
                jsonDict = convert_from_svg_to_json(file_contents, file_name)
                with open(out + file_path.strip(".svg") + ".json", "w") as file:
                    json.dump(jsonDict, file, indent=4)
    else:
        file_name = out + str(json_file) + ".svg"
        with open(file_name, 'r') as file:
            # Read the entire file into a string
            file_contents = file.read()
            jsonDict = convert_from_svg_to_json(file_contents, file_name)
            output_file = file_name.replace(".svg", "") + ".json"
            with open(output_file, "w") as file:
                json.dump(jsonDict, file, indent=4)