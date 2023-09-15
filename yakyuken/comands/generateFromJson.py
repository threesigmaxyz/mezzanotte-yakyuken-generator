import os
import random

import click
import tqdm

from yakyuken.core import regenerate_nft


@click.command("generate_from_json")
@click.option(
    "--json_file", default=0, show_default=True, help="TokenId of the jsonFile to re-generate the .svg"
)
@click.option(
    "--all_files", default=False, show_default=True, help="True to re-generate all the json files from the out folder to svg."
)
@click.option(
    "--dir",
    type=click.Path(file_okay=False),
    default="out",
    show_default=True,
    help="Directory where the json files are.",
)
def regenerate_command(json_file: int, dir: click.Path, all_files: bool) -> None:
    if all_files == True:
        # List all files in the folder
        files = os.listdir(dir)

        # Filter for .json files
        json_files_list = [file for file in files if (file.endswith(".json") and "byte" not in file )]

        for file in json_files_list:
            token_Id = int(file.replace(".json", ""))
            newNft = regenerate_nft(dir + "/" + file,token_Id)

            filepath = os.path.join(dir, f"{json_file}.svg")
            with open(filepath, "w") as f:
                f.write(newNft)
    else:
        file_name = dir + "/" + str(json_file) + ".json"
        newNft = regenerate_nft(file_name, json_file)
        filepath = os.path.join(dir, f"{json_file}.svg")
        with open(filepath, "w") as f:
            f.write(newNft)