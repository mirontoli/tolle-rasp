#!/usr/bin/python3
import os
import time

#flite is a simple speech synthesator

for i in range(1,11):
  os.system("flite -t '%s'" % i)
  time.sleep(1)
