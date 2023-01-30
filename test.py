#!/usr/bin/env python3

import logging
import subprocess
import ruamel.yaml
from pathlib import Path
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:\
                    %(lineno)s:%(funcName)2s(): %(message)s', level=logging.DEBUG)
def my_function():
    logging.info('This message should go to the log file')
  
for i in range(5):
    print(i)
dicts={'color': 'blue', 'fruit': 'apple'}
for k,v in dicts.items():
    if not isinstance(v,dict):
        print(k,":",v)
    else:
        for kk,vv in v.items():
            print("  ",kk,":",vv)

tmp="good"
if tmp=="good":
    print("matched")

cmd ="ls -al"
result=subprocess.run(cmd, stdin=subprocess.PIPE, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT, universal_newlines=True, check=True)
print("stdout:", result.stdout)
print("stderr:", result.stderr)
myyaml = ruamel.yaml.YAML()
data = myyaml.load(Path('myfile.yml').read_text())
with open("structure.yml", "w") as file:
    myyaml.indent(sequence=4, offset=2)
    myyaml.dump(data, file)
if __name__ == "__main__":
    my_function()
