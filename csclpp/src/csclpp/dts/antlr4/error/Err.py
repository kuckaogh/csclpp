from __future__ import print_function
import os, sys


errFile= ''

errors=[]

        
def addError(msg, where1, where2):
    errors.append(msg)
    print ('#Error: '+where1+': '+where2+': '+msg, file=sys.stderr)       
        