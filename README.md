# Mezzanotte Yakyuken Generator [![Github Actions][gha-badge]][gha] [![License: MIT][license-badge]][license]

[gha]: https://github.com/threesigmaxyz/mezzanotte-yakyuken-generator/actions
[gha-badge]: https://github.com/threesigmaxyz/mezzanotte-yakyuken-generator/actions/workflows/main.yml/badge.svg
[license]: https://opensource.org/licenses/MIT
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg

![banner](./resources/banner/ts-my-banner.jpeg)

This repository contains the source code for a CLI tool for generating Mezzanotte Yakyuken NFTs.

## Installation
To install the CLI tool, you can use pip package manager. Open your terminal and run the following commands:
```bash
git clone https://github.com/threesigmaxyz/mezzanotte-yakyuken-generator.git
cd mezzanotte-yakyuken-generator
pip install -e .
```
This command will download and install the latest tool version along with its dependencies.

Once the installation is complete, you can verify that the installation was successful by running the following command:
```bash
yakyuken --help
```
If the installation was successful, this command will display the help menu of the CLI tool.

## Configuration
The CLI tool will load configuration regarding the NFTs from a JSON file, located at `generator.config.json`.

In order to modify any of the NFTs' attributes, you can edit the configuration file directly.

**Example:**
```json
{
   "metadata": {
      "texts": [
         { "value": "石", "weight": 50 },
         { "value": "はさみ", "weight": 50 }
      ]
   }
}
```
Partially changing the configuration file to will distribute the text trait between `石` and `はさみ` with a 50% probability each.


__Note that the sum of all `weight` entries for a given trait must add to 100.__

## Getting Started
The `generate` command can be used to generate random NFTs based on a configuration file.

**Options:**
- `--count`: Number of NFTs to generate. (default: 1)
- `--out`:  Output directory.  (default: out])
- `--seed`: Seed for the random generator. (default: None)

**Example:**
```bash
yakyuken generate --count=2 --out="./out" --seed=1337
```
The following command will generate 2 NFTs and save the SVG files to the `./out` directory.

__Note that reusing the `seed` value will result in the same NFTs being generated.__


## About Us
[Three Sigma](https://threesigma.xyz/) is a venture builder firm focused on blockchain engineering, research, and investment. Our mission is to advance the adoption of blockchain technology and contribute towards the healthy development of the Web3 space.

If you are interested in joining our team, please contact us [here](mailto:info@threesigma.xyz).

---

<p align="center">
    <a href="https://threesigma.xyz" target="_blank">
        <img src="https://threesigma.xyz/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fthree-sigma-labs-research-capital-white.0f8e8f50.png&w=2048&q=75" width="75%" />
    </a>
</p>