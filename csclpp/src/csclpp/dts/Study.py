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
    newArrayList = []
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
        self.newArrayList=[]
        self.newConstMap=collections.OrderedDict()
        self.metaData={}
        self.start_earliest=None
        self.end_latest=None

