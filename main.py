import sys
 import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_)+'/src'))) 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_) + '/tests' )))



#from care import get_answer from core import main
from core import main
if_name=='__main_':
  f = open("packets/tcp.txt","r") 
  B = open('packets/udp.txt','r')
  main(f)
