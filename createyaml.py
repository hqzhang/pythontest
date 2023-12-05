#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
#conf = yaml.safe_load(Path('data.yml').read_text())

file="/Users/hongqizhang/workspace/pythontest/work"
#def parse(file):
def readCompList(file):
    myyaml = ruamel.yaml.YAML()
    data = myyaml.load(Path(file+'/configuration.yml').read_text())
    print(data)
    dict={}
    for var in data['components']:
        if var['type'] not in dict:
            dict[var['type']]= [ var['name']]
        else:
            dict[var['type']].append(var['name'])
    return dict

print( readCompList(file) )