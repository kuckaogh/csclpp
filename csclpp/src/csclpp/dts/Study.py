import sys
from collections import defaultdict
import collections

class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}
    varExprMap = {}
    tempVarList = []
    ifsMap = {}
    newArrayList = []
    newConstMap = collections.OrderedDict()

    metaData =''

    def __init__(self):
        self.data_src=[]
        self.varFile=''
        self.varDef=''
        self.varPathMap={}
        self.varExprMap={}
        self.ifsMap={}
        self.newArrayList=[]
        self.newConstMap=collections.OrderedDict()
        self.metaData=''


