#!/usr/bin/env python3
import sys
import yaml
import ruamel_yaml
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

myyaml = ruamel.yaml.YAML()
data = myyaml.load(Path('myfile.yml').read_text())
print(data)
data['locations'][0]['ip Addr']='HQmyip8.8.8.8999'
print('tag', data['locations'][0].tag.value)
print(data['locations'][0])
print(data['locations'][0]['Id'])
mydt=data['locations']
for i in range(2):
  if mydt[i]['Id']=='i-b':
    print(mydt[i]['ipAddr'])


with open("structure.yml", "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)
