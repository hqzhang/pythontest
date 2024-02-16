#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
#conf = yaml.safe_load(Path('data.yml').read_text())

file="/Users/hongqizhang/workspace/pythontest"

def readCompList(file):
    myyaml = ruamel.yaml.YAML()
    data = myyaml.load(Path(file+'/config.yaml').read_text())
    print(data)
    dict={}
    for var in data['components'][:]:
       print(var)
       if var['type']=='daemon':
           print(var)
           data['components'].remove(var)
    print(data)

readCompList(file)
