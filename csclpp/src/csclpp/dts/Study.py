import sys
from collections import defaultdict
import collections

class Study:

    data_src=[]   # e.g., dss file path
    varFile=''
    varDef=''
    varPathMap = {}
    varExprMap = collections.OrderedDict()
    varSystemMap = {}
    tempVarList = []
    ifsMap = {}
    newArrayMap = collections.OrderedDict()
    newConstMap = collections.OrderedDict()

    metaData ={}
    start_earliest=None
    end_latest=None


    def __init__(self):
        self.data_src=[]
        self.varFile=''
        self.varDef=''
        self.varPathMap={}
        self.varExprMap=collections.OrderedDict()
        self.varSystemMap = {}
        self.ifsMap={}
        self.newArrayMap=collections.OrderedDict()
        self.newConstMap=collections.OrderedDict()
        self.metaData={}
        self.start_earliest=None
        self.end_latest=None

