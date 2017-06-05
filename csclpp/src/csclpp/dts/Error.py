import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import os

errors=[]

        
def addError(msg):
    errors.append(msg)
    print ('#Error: '+msg)       
        