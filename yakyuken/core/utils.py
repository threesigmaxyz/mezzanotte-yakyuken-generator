import json
import random

from typing import Any, Dict, List, Optional, Tuple, Union
import re

STARS = 'd="M166.391'
ABSTRACT = 'd="M82.19'
SCRIBBLE = 'd="M11.213'

AMI = 'd="M418'
CHRISTINE = 'd="M438'
FOCUSED_GIRL= 'd="M17'
JOSEI = 'd="M5 0C3'
REDLADY = 'd="M136'
SPORT = 'd="M531'
TAKECHI = 'd="M466'
TENNIS = 'd="m408'
THINKER = 'd="M312'
YAK2 =  'd="m213'


def load_config(filepath: str) -> Dict[str, Any]:
    """Load config file."""
    with open(filepath, "r") as f:
        return json.load(f)


def load_svg_path(filepath: str) -> str:
    """Load SVG path from file."""
    with open(filepath, "r") as f:
        return f.read()


def parse_trait_values(
    trait_values: List[dict],
) -> Tuple[List[object], Optional[List[int]]]:
    """Parse trait values from config file."""
    return (
        [trait_value["value"] for trait_value in trait_values],
        [trait_value["weight"] for trait_value in trait_values],
    )


def select_trait_value(trait_metadata: List[Dict[str, Union[str, int]]]) -> Any:
    """Randomly select trait value from weighted options."""
    values, weights = parse_trait_values(trait_metadata)

    assert sum(weights) == 100, "Probability distribution weights must sum to 100."
    weights = weights if weights is not None else [1 / len(values)] * len(values)

    return random.choices(values, weights=weights)[0]


def get_match_regex(file_content: str, regex: str) -> str:
    match = re.search(regex, file_content)
    if match:
        value = match.group(1).strip()
    else:
        value = "ERROR"
        print("Value not found.")

    return value

def get_yak(file_content):
    if AMI in file_content:
        return("ami")
    elif CHRISTINE in file_content:
        return("christine")
    elif FOCUSED_GIRL in file_content:
        return("focusedgirl")
    elif JOSEI in file_content:
        return("josei")
    elif REDLADY in file_content:
        return("redlady")
    elif SPORT in file_content:
        return("sport")
    elif TAKECHI in file_content:
        return("takechi")
    elif TENNIS in file_content:
        return("tennis")
    elif THINKER in file_content:
        return("thinker")
    elif YAK2 in file_content:
        return("yak2")
    else:
        print("Error getting the yak")
        return("ERROR")

def get_icon(file_content) -> str:
    if STARS in file_content:
        return("stars")
    elif ABSTRACT in file_content:
        return("abstract")
    elif SCRIBBLE in file_content:
        return("scribble")
    else:
        return("none")