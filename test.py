#!/usr/bin/env python3

import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(funcName)2s(): %(message)s', level=logging.DEBUG)
log = logging.getLogger()
import sys
import time
#logging.basicConfig( encoding='utf-8', level=logging.DEBUG)
def my_function():
  print("Hello from a function")
  logging.debug('This message should go to the log file')
  log.debug('This message should go to the log file')
def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    #text = input("Yell something at a mountain: ")
    #print(echo(text))
    my_function()
    print(sys.argv[1])
