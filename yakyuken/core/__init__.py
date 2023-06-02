from yakyuken.core.utils import (
    load_config,
    load_svg_path,
    parse_trait_values,
    select_trait_value,
)


# Load config file.
config = load_config("generator.config.json")

# Extract config values.
yaks = config["yaks"]
icons = config["icons"]
metadata = config["metadata"]

# Load SVG paths from config values.
yak_paths = {yak["value"]["path"]: load_svg_path(yak["value"]["path"]) for yak in yaks}
icon_paths = {
    icon["value"]["path"]: load_svg_path(icon["value"]["path"]) for icon in icons
}


def generate_nft() -> str:
    """Generate an NFT."""
    # Select common trait values.
    background_color = select_trait_value(metadata["backgroundColors"])
    base_fill_color = select_trait_value(metadata["baseFillColors"])
    initial_shadow_color = select_trait_value(metadata["initialShadowColors"])
    final_shadow_color = select_trait_value(metadata["finalShadowColors"])
    glow_time = select_trait_value(metadata["glowTimes"])

    # Select yak trait values.
    yak = select_trait_value(yaks)
    yak_path = yak_paths[yak["path"]]
    yak_fill_color = select_trait_value(metadata["yakFillColors"])
    yak_hover_color = select_trait_value(metadata["hoverColors"])

    # Select icon trait values.
    icon = select_trait_value(icons)
    icon_path = icon_paths[icon["path"]]
    icon_color = yak_fill_color   # TODO icon["color"]
    icon_size = yak["iconSize"]
    icon_location = select_trait_value(metadata["iconLocations"])

    # Select text trait values.
    text_content = select_trait_value(metadata["texts"])
    text_size = yak["fontSize"]
    text_location = select_trait_value(metadata["textLocations"])

    # Generate SVG file content.
    nft = f"""<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet" viewBox="{yak["viewBox"]}"
    style="background-color:{background_color}"> 
        <style>
            @keyframes glow {{
                0% {{
                    filter: drop-shadow(16px 16px 20px {initial_shadow_color}) brightness(100%);
                }}

                to {{
                    filter: drop-shadow(16px 16px 20px {final_shadow_color}) brightness(200%);
                }}
            }}

            path {{
                fill: {base_fill_color};
                animation: glow {glow_time}s ease-in-out infinite alternate;
            }}

            .yak {{
                fill: {yak_fill_color};
            }}

            .yak:hover {{
                fill: {yak_hover_color};
            }}

            .icon {{
                fill: {icon_color};
            }}
        </style>  
        {yak_path}

        <svg {icon_size} {icon_location}>
            {icon_path}
        </svg>

        <text text-anchor={text_location} font-family="Helvetica" font-size="{text_size}" fill="white">
            {text_content}
        </text>
    </svg>"""

    return nft
