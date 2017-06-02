import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import os
import csv

        
def printCSV(studyVarTs):

    for s in studyVarTs:
        d = studyVarTs[s]
        with open(s+".csv", "wb") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(d.keys())
            writer.writerows(zip(*d.values()))  
        outfile.close()        
        