import os
import sys
import time

f = open('names.txt', 'r')
'''
  one line would read: "username password"
'''

Lines = f.readlines()

for line in Lines:
  user, password = line.split()
  cmdUser = 'useradd ' + user
  cmdPasswd = 'passwd ' + user
  cmdEchoPasswd = 'echo ' + password
  os.system(cmdUsr)
  os.system(cmdPasswd)
  time.sleep(.5)
  os.system(cmdEchoPasswd)
  time.sleep(.5)
  os.system(cmdEchoPasswd)
