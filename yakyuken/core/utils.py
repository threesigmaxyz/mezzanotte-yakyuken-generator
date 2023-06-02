import json
import random

from typing import Any, Dict, List, Optional, Tuple, Union


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
