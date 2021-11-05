#!/bin/python

import sys
from typing import Union
import typing

import yaml


def dfs(prefix: str, node: Union[bool, int, float, str, list, dict]):
    if type(node) == bool:
        bool_value = 'true' if node else 'false'
        print(f"{prefix} = {bool_value}")
    elif type(node) in {int, float, str}:
        print(f"{prefix} = {node}")
    elif type(node) == list:
        for i, obj in enumerate(node):
            dfs(f'{prefix}[{i}]', obj)
    elif type(node) == dict:
        for key, obj in node.items():
            dfs(key if len(prefix) == 0 else f'{prefix}.{key}', obj)



if __name__ == '__main__':
    yaml_file: str = sys.argv[1]

    with open(yaml_file, 'r', encoding='utf-8') as yf:
        orig_data: str = yf.read()
        dfs("", yaml.safe_load(orig_data))
