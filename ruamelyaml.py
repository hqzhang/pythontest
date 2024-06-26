#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
myyaml = ruamel.yaml.YAML()
data = myyaml.load(Path('configuration.yaml').read_text())
print(data)
with open("output.yml", "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)

config="""
components:
   name:
   Path:
   LaunchScript:
   executable: 
   jvm_cp: 
   java_cp:
   type:
"""
daemon="""

"""

cfg= ruamel.yaml.YAML().load(config)
keys=list(cfg['components'].keys())
print(keys)
lss=[]
for var in data['components']:
   mydict={}
   for key in keys:
      for k, v in var.items():
         if isinstance(v, dict):
            for kk,vv in v.items():
                  if key==kk:
                     mydict[key]= vv
         else:
            if key==k:
                 mydict[key]= v
   lss.append(mydict)              
print(lss)

class Employee(yaml.YAMLObject):
    yaml_tag = u'!Employee'

    def __init__(self, name, age):
        self.name = name
        self.age = age

yaml_string = """
employees:
  - !Employee
    name: John Doe
    age: 30
  - !Employee
    name: Jane Smith
    age: 25
"""

data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(data)

