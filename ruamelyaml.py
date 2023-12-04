#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
myyaml = ruamel.yaml.YAML()
data = myyaml.load(Path('configsolution.yaml').read_text())
print(data)

source = myyaml.load(Path('configuration.yaml').read_text())
print(source)

for ched in data['components']:
    for src in source['components']:
          if ched == src:
                for 
                print ( ched )

with open("output.yml", "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)
