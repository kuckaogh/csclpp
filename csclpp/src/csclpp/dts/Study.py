import sys


class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}
    varExprMap = {}
    metaData =''

    def __init__(self):
        self.varMap={}


