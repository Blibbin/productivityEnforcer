import platform
import os
import subprocess
from pathlib import Path
# import pypykatz
import sys
from tools import key
import re

import random



def detectOS():
    return platform.system()

def parseAttack(os):
    match os:
        case 'Linux':
            return

def tokenizeData():

    return

def dumpSSH():
    
    # titles = os.system("cat | ")
    # x = os.system("cat ~/.ssh/config")
    SSH = []

    directory = Path("~/.ssh/test").expanduser()

    for file_path in directory.iterdir():
        print(file_path)
        if file_path.is_file() and '.pub' not in file_path.name:
            SSH.append([file_path.name, file_path.name + '.pub'])
            with open(file_path, "r") as f:
                content = f.read()
                print(content)
                # SSH.append([file_path.name, content])
                # SSH.append([])
            
            with open(file_path.with_suffix('.pub'), "r") as f:
                content = f.read()
                print(content)

    # _size = len(SSH)
    # key = random.randrange(0, _size - 1)
    # print(SSH[key])

    print(SSH)
