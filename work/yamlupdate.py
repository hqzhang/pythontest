#!/usr/bin/env python3
import sys
import yaml
import ruamel.yaml
from pathlib import Path
import logging as log
params={}
log.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:\
  %(lineno)s:%(funcName)2s(): %(message)s', level=log.NOTSET)
def parseConfig(fileName):
    log.info("Enter parseConfig() ")
    global params
    myyaml = ruamel.yaml.YAML()
    params = myyaml.load(Path(fileName).read_text())
    print(params)
    for var in params['components']:
        for k,v in var.items():
          if not isinstance(v,dict):
            print(k,v)
          else:
            for kk,vv in v.items():
              print(kk,vv)
def updateConfiguration(fileName,output):
    log.info("Enter updateConfiguration() ")
    myyaml = ruamel.yaml.YAML()
    data = myyaml.load(Path(fileName).read_text())
    print(data)
    for var in data['components']: 
        #while compoent name is matching
        for comp in params['components']:
          if comp['name'] == var['name']:
            print('Seting in ',var['name'],'SETTING Just if Existing')
            for k,v in comp.items():
              if not isinstance(v,dict):
                if k in var:
                  print("set ",k, "as",v)
                  var[k]=v
                  print(var)
              else: 
                 for kk,vv in v.items():
                    if kk in var[k]:
                      print("set ",kk, "as",vv)
                      var[k][kk]=vv
                      print(var)

    saveFile(output,data)

def saveFile(output,data):
  with open(output, "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)

if __name__ == "__main__":
   parseConfig('config')
   updateConfiguration('configuration.yml','configuration_out.yml')
