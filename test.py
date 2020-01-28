import os
import sys

dir = sys.exec_prefix
fil = []

for i in os.walk(dir):
    fil.append(i)

for address, dirs, files in fil:
    for file in files:
        if file == 'pyuic5.bat':
            print(address+'\\'+file)