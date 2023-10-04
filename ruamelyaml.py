#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
myyaml = ruamel.yaml.YAML()
data = myyaml.load(Path('config.yml').read_text())
print(data)

data = myyaml.load(Path('structure.yml').read_text())
print(data)


with open("output.yml", "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)
