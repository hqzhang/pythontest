#!/usr/bin/env python3
import sys

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
    
def dictUpdate(var,comp):
    print('Enter dictUpdate() config:',comp)
    for k,v in comp.items():
      if not isinstance(v,dict):
        for x,y in var.items():
          print("x,k:",x,k)
          if x in k:
            print("set ",k, "as",v)
            var[x]=v
      else: 
          for kk,vv in v.items():
            for x,y in var[k].items():
              if x in kk:
                    print("set ",kk, "as",vv)
                    var[k][x]=vv
    print("END:",var)
    return var

def updateConfiguration(fileName,output):
    
    log.info("Enter updateConfiguration() ")
    global params
    myyaml = ruamel.yaml.YAML()
    data = myyaml.load(Path(fileName).read_text())
    #print(data)
    for var in data['components']: 
       print('comp==',var)
       for kk, vv in var.items():
          for key,val in params['components'][0].items(): #for template
             if  key == kk and isinstance(val,dict):
                for kkk, vvv in vv.items():
                     if kkk not in val:
                        print('catch=',kkk)
                        params['components'][0][key][kkk]=vvv  
    saveFile(output,params)

def saveFile(output,data):
  with open(output, "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)



if __name__ == "__main__":
    parseConfig('config')
    updateConfiguration('configuration.yml','configuration_out.yml')
  
    # Use the update method to merge dict2 into dict1
   
   

