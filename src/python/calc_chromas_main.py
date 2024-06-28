from pathlib import Path

from calc_chromas import calc_chromas
from read_yaml import read_yaml
from tone_chroma_coefficient_dict import TONE_CHROMA_COEFFICIENT_DICT
from write_yaml import write_yaml


def main() -> None:
    """_summary_"""
    yaml_path = Path(input()).resolve()
    yaml_data = read_yaml(yaml_path)
    for hue in range(0, 360, 15):
        chroma = float(yaml_data["rgb"][f"{hue=}"]["v"]["chroma"])
        for tone, chroma_coefficient in TONE_CHROMA_COEFFICIENT_DICT.items():
            yaml_data["rgb"][f"{hue=}"][tone]["chroma"] = calc_chromas(chroma)[
                chroma_coefficient
            ]
    write_yaml(yaml_data, yaml_path)


if __name__ == "__main__":
    main()
