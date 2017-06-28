import sys
from collections import defaultdict
import collections

class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}

    varSystemMap = {}
    tempVarList = []
    ifsMap = {}

    strArrayMap = collections.OrderedDict()
    intArrayMap = collections.OrderedDict()
    floatArrayMap = collections.OrderedDict()        
    constMap = collections.OrderedDict()

    metaData ={}
    start_earliest=None
    end_latest=None


    def __init__(self):
        self.data_src=[]
        self.varFile=''
        self.varDef=''
        self.varPathMap={}

        self.varSystemMap = {}
        self.ifsMap={}

        self.strArrayMap=collections.OrderedDict()  
        self.intArrayMap=collections.OrderedDict()  
        self.floatArrayMap=collections.OrderedDict()        
        self.constMap=collections.OrderedDict()
        self.metaData={}
        self.start_earliest=None
        self.end_latest=None

