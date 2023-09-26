import os
import random

import click
import tqdm

from yakyuken.core import generate_nft


@click.command("generate")
@click.option(
    "--count", default=1, show_default=True, help="Number of NFTs to generate."
)
@click.option(
    "--out",
    type=click.Path(file_okay=False),
    default="out",
    show_default=True,
    help="Output directory.",
)
@click.option("--seed", type=int, help="Seed for random generator.")
def generate_command(count: int, out: click.Path, seed: int) -> None:
    """
    Generate a Yakyuken NFTs.
    """
    # Initialize output directory.
    out = out.name if isinstance(out, click.Path) else out
    os.makedirs(out, exist_ok=True)

    # Set random seed.
    if seed is not None:
        random.seed(seed)

    for i in tqdm.tqdm(range(count)):
        # Generate NFT.
        nft = generate_nft(i)

        # Write NFT to file.
        filepath = os.path.join(out, f"{i}.svg")
        with open(filepath, "w") as f:
            f.write(nft)
