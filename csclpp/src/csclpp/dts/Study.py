import sys


class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}
    varExprMap = {}
    metaData =''

    def __init__(self):
        self.data_src=[]
        self.varFile=''
        self.varDef=''
        self.varPathMap={}
        self.varExprMap={}
        self.metaData=''


