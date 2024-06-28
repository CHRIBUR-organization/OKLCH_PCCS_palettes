from collections import OrderedDict
from pathlib import Path
from typing import Any

from constant_for_yaml_read_write_option import CONSTANT_FOR_YAML_READ_WRITE_OPTION
from yaml import (
    Dumper,
    FullLoader,
    Loader,
    Node,
    UnsafeLoader,
    add_constructor,
    add_representer,
    unsafe_load,
)


def read_yaml(yaml_path: Path) -> Any:
    """_summary_

    Parameters
    ----------
    yaml_path : Path
        _description_

    Returns
    -------
    Any
        _description_

    """

    def represent_ordered_dict(dumper: Dumper, instance: OrderedDict[Any, Any]) -> Node:
        return dumper.represent_mapping(
            CONSTANT_FOR_YAML_READ_WRITE_OPTION, instance.items()
        )

    add_representer(OrderedDict, represent_ordered_dict)

    def construct_ordered_dict(
        loader: Loader | FullLoader | UnsafeLoader, node: Node
    ) -> Any:
        return OrderedDict(loader.construct_pairs(node))

    add_constructor(CONSTANT_FOR_YAML_READ_WRITE_OPTION, construct_ordered_dict)
    with Path.open(yaml_path) as f:
        return unsafe_load(f)
