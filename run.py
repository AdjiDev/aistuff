"""

JANGAN LUPA BINTANG NYA WOYY

"""

import platform
import os
import sys
import time

def bersihkan():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def ngetik(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def init():
    while True:
        ngetik('type aili --setup to install module\nafter all module installed type aili --run\n\n# Version beta_0.0.1\ntype exit/quit to exit\n\n\n')
        perintahnyacok = input('(init/)~$ ')
        if perintahnyacok == 'aili --setup':
            os.system('pip install -r install.txt')
        elif perintahnyacok == 'aili --run':
            os.system('python main.py')
        elif perintahnyacok == 'exit':
            ngetik('exit . . .')
            break
        elif perintahnyacok == 'quit':
            ngetik('exit . . .')
            break
        else:
            print('invalid command')

bersihkan()
init()
