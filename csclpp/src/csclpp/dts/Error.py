import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import os

errors=[]

        
def addError(msg, where1, where2):
    errors.append(msg)
    print ('#Error: in '+where1+': '+where2+': '+msg)       
        