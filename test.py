#!/usr/bin/env python3

import logging
import subprocess
import ruamel.yaml
import yaml
from xml.dom.minidom import parseString

from collections import OrderedDict
from pathlib import Path
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:\
%(lineno)s:%(funcName)2s(): %(message)s', level=logging.DEBUG)
def myfunc():
    logging.info('This message should go to the log file')

#create dictionary:
yml="""name: hongqi
age: 18"""
config="""components:
-  !components
   name: hong
   executable: Java-99
   settings:
        pages: 120
        author: emily
"""
ymltag="""
components:
-  !components
   name: hong
   executable: JAVA
   settings:
        pages: 100
        date: 2024-02
  """
data= ruamel.yaml.YAML().load(ymltag)
cfg= ruamel.yaml.YAML().load(config)
#print(data.update(cfg))
#print(data)

for var in data['components']: 
       print(var)
        #when compoent name is matching
       for cfg in cfg['components']:
          if cfg['name'] == var['name']:
             var.update(cfg)
             
print(data)
exit()

json={ 'name': 'hong','age': 18}
list=[('name','hongqi'),('age',18)]
myxml="""
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
"""
mydict6=parseString(myxml) 
print(mydict6)
mydict2=OrderedDict( yaml.safe_load(yml) )
mydict3=OrderedDict(json)
mydict4=OrderedDict(list)
mydict5=OrderedDict(name='hong',age=18)
for i in range (1,6):
    print(eval("mydict" + str(i)))

eval( """print("Hello")""")

#get all keyv
for k,v in mydict1.items():
    if not isinstance(v,dict):
        print(k,":",v)
    else:
        for kk,vv in v.items():
            print("  ",kk,":",vv)
tmp=["good","look"]
if "good" in tmp:
    print("Find it")
cmd ="hostname"
result=subprocess.run(cmd, stdin=subprocess.PIPE, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.STDOUT, universal_newlines=True, check=True)
print("stdout:", result.stdout)
print("stderr:", result.stderr)
myyaml = ruamel.yaml.YAML()
#data = myyaml.load(Path('myfile.yml').read_text())
with open("structure.yml", "w") as file:
    myyaml.indent(sequence=4, offset=2)
#   myyaml.dump(data, file)
myvar=10
print( eval("myvar") )
if __name__ == "__main__":
    myfunc()
