#!/usr/bin/env python3

import ruamel.yaml
from pathlib import Path

    
myyaml = ruamel.yaml.YAML()
yaml_str=Path('myfile.yml').read_text()
data = myyaml.load(yaml_str)

for idx, x in enumerate(data['machines']):
    print(x)
    if idx==1:
        data['machines'].remove(x)
        

print(data)
#with open("structure.yml", "w") as file:
 #       # yaml.dump need a dict and a file handler as parameter
 #       myyaml = ruamel.yaml.YAML()
 #       myyaml.indent(sequence=4, offset=2)
 #       myyaml.dump(data, file)

