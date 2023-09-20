from yakyuken.core.utils import (
    load_config,
    load_svg_path,
    parse_trait_values,
    select_trait_value,
)

import json


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


def generate_nft(token_Id: int) -> str:
    """Generate an NFT."""
    # Select common trait values.
    background_color = select_trait_value(metadata["backgroundColors"])
    base_fill_color = select_trait_value(metadata["baseFillColors"])
    initial_shadow_color = select_trait_value(metadata["initialShadowColors"])
    initial_shadow_brightness = select_trait_value(metadata["initialShadowBrightness"])
    final_shadow_color = select_trait_value(metadata["finalShadowColors"])
    final_shadow_brightness = select_trait_value(metadata["finalShadowBrightness"])
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

    # Select text trait values.
    text_content = select_trait_value(metadata["texts"])

    data = {
        "tokenId": token_Id,
        "backgroundColors": background_color,
        "baseFillColors": base_fill_color,
        "initialShadowColors": initial_shadow_color,
        "initialShadowBrightness": initial_shadow_brightness,
        "finalShadowColors": final_shadow_color,
        "finalShadowBrightness": final_shadow_brightness,
        "glowTimes": glow_time,
        "yaks": yak["name"],
        "yakFillColors": yak_fill_color,
        "hoverColors": yak_hover_color,
        "icons": icon["name"],
        "texts": text_content
    }

    # Specify the file path where you want to save the JSON data
    file_path = "out/"+ str(token_Id) +".json"

    # Write the data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Generate SVG file content.
    nft = f"""<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet" viewBox="{yak["viewBox"]}"
    style="background-color:{background_color}"> 
        <style>
            @keyframes glow {{
                0% {{
                    filter: drop-shadow(16px 16px 20px {initial_shadow_color}) brightness({initial_shadow_brightness}%);
                }}

                to {{
                    filter: drop-shadow(16px 16px 20px {final_shadow_color}) brightness({final_shadow_brightness}%);
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

        <svg {icon_size} x=\"5%\" y=\"5%\">
            {icon_path}
        </svg>

    </svg>"""

    return nft



def convert_json_to_bytes(json_file_path: str) -> (int, str):
    dataBytes = {
        "tokenId": None,
        "backgroundColors": None,
        "baseFillColors": None,
        "initialShadowColors": None,
        "initialShadowBrightness": None,
        "finalShadowColors": None,
        "finalShadowBrightness": None,
        "glowTimes": None,
        "yaks": None,
        "yakFillColors": None,
        "hoverColors": None,
        "icons": None,
        "texts": None
    }

    with open(json_file_path, "r") as json_file:
        # Load the JSON data from the file into a Python dictionary or list
        dataJson = json.load(json_file)

    for key in metadata.keys():
        for i, element in enumerate(metadata[key]):
            if key in dataJson and dataJson[key] == element["value"]:
                dataBytes[key] = str(hex(i))[2:] # so "0x" is not included in the string
    
    for i, yak in enumerate(yaks):
        if dataJson["yaks"] == yak["value"]["name"]:
            dataBytes["yaks"] = str(hex(i))[2:] # so "0x" is not included in the string

    for i, icon in enumerate(icons):
        if dataJson["icons"] == icon["value"]["name"]:
            dataBytes["icons"] = str(hex(i))[2:] # so "0x" is not included in the string 
    
    dataBytes["tokenId"] = dataJson["tokenId"]

    if int(dataBytes["glowTimes"], 16) <= 0xF:
        dataBytes["glowTimes"] = "0" + dataBytes["glowTimes"]
    
    
    if int(dataBytes["backgroundColors"],16) <= 0xF:
        dataBytes["backgroundColors"] = "0" + dataBytes["backgroundColors"]
    

    output = "0x" + dataBytes["glowTimes"] + dataBytes["backgroundColors"] + dataBytes["hoverColors"] + dataBytes["finalShadowColors"] + dataBytes["baseFillColors"] + dataBytes["yakFillColors"] + dataBytes["yaks"] + dataBytes["initialShadowColors"] + dataBytes["initialShadowBrightness"] + dataBytes["finalShadowBrightness"] + dataBytes["icons"] + dataBytes["texts"]
    print(dataBytes)
    print(output)
    if(len(output) != 16):
        print("ERROR: final bytes conversion does not have expected length - ", output)
    return (dataBytes["tokenId"], output)


def regenerate_nft(json_file_path: str, tokenId: int) -> str:
    with open(json_file_path, "r") as json_file:
        # Load the JSON data from the file into a Python dictionary or list
        dataJson = json.load(json_file)

    relevant_icon, relevant_yak = "", ""
    # Generate SVG file content.
    for yak in yaks:
        if yak["value"]["name"] == dataJson["yaks"]:
            relevant_yak = yak

    for icon in icons:
        if icon["value"]["name"] == dataJson["icons"]:
            relevant_icon = icon

    if relevant_icon == "" or relevant_yak == "":
        print("ERROR: Relevant Icon or Relevant Yak not recognized")
        exit()

    nft = f"""<svg xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet" viewBox="{relevant_yak["value"]["viewBox"]}"
    style="background-color:{dataJson["backgroundColors"]}"> 
        <style>
            @keyframes glow {{
                0% {{
                    filter: drop-shadow(16px 16px 20px {dataJson["initialShadowColors"]}) brightness({dataJson["initialShadowBrightness"]}%);
                }}

                to {{
                    filter: drop-shadow(16px 16px 20px {dataJson["finalShadowColors"]}) brightness({dataJson["finalShadowBrightness"]}%);
                }}
            }}

            path {{
                fill: {dataJson["baseFillColors"]};
                animation: glow {dataJson["glowTimes"]}s ease-in-out infinite alternate;
            }}

            .yak {{
                fill: {dataJson["yakFillColors"]};
            }}

            .yak:hover {{
                fill: {dataJson["hoverColors"]};
            }}

            .icon {{
                fill: {relevant_icon["value"]["color"]};
            }}
        </style>  
        {yak_paths[relevant_yak["value"]["path"]]}

        <svg {relevant_yak["value"]["iconSize"]} x=\"5%\" y=\"5%\">
            {icon_paths[relevant_icon["value"]["path"]]}
        </svg>
    </svg>"""

    return nft



