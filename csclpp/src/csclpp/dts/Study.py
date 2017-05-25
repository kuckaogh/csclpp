import sys


class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}
    varExprMap = {}
    tempVarList = []
    ifsMap = {}
    newArrayList = []

    metaData =''

    def __init__(self):
        self.data_src=[]
        self.varFile=''
        self.varDef=''
        self.varPathMap={}
        self.varExprMap={}
        self.ifsMap={}
        self.newArrayList=[]
        self.metaData=''


