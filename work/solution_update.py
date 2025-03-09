#!/usr/bin/env python3
import sys
import ruamel_yaml
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

def updateConfiguration(input,config, output):
    print("Enter updateConfiguration() ", input, config)
    myyaml = ruamel.yaml.YAML()
    data = myyaml.load(Path(input).read_text())
    print("data=",data['components'])
    param = myyaml.load(Path(config).read_text())
    print("param=",param['components'][0])
    for var in data['components']: # new data
       for kk, vv in var.items():
          #print('kk=',kk)

          if kk not in param['components'][0]:
             #print('catch=', kk)
             param['components'][0][kk]=vv
          for key,val in param['components'][0].items(): # template data
             if  key == kk and isinstance(val,dict):
                for kkk, vvv in vv.items():
                     if kkk not in val:
                        print('catch=',kkk)
                        param['components'][0][key][kkk]=vvv
    for var in data['daemonalloc'].items(): # new data
        print('var=====',var[0])
        #for kv in param['daemonalloc'].items():
        if var[0] not in param['daemonalloc']:
           print('catch=', var[0])
           param['daemonalloc'][var[0]]=var[1]

    saveFile(output,param)

def saveFile(output,data):
  with open(output, "w") as file:
        # yaml.dump need a dict and a file handler as parameter
        myyaml = ruamel.yaml.YAML()
        myyaml.indent(sequence=4, offset=2)
        myyaml.dump(data, file)



if __name__ == "__main__":
    #parseConfig('config.yaml')
    updateConfiguration('configuration.yaml', 'config.yaml','configuration_out.yml')
  
    # Use the update method to merge dict2 into dict1
   
   

