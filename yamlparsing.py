#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
#conf = yaml.safe_load(Path('data.yml').read_text())
yaml_str = """\
steps:
- !<!entry>
  id: Entry-1
  actions: []
- !<!replybuttons>
  id: ReplyButtons-langcheck
  footer: ''
"""
with open("myfile.yml", "r") as myfile:
    mydic=yaml.safe_load(myfile)
    print(mydic)
    
myyaml = ruamel.yaml.YAML()
yaml_str=Path('myfile.yml').read_text()
data = myyaml.load(yaml_str)
data['locations'][0]['ip Addr']='myip8.8.8.8999'
#print('tag', data['steps'][1].tag.value)


with open("structure.yml", "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)

