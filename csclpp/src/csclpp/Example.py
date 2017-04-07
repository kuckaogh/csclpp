import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Temp as T
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *



# parse setting file and vardef
studyMap = W.setupReference('./example_data/sample.setting')



studyVarData = {} # studyName, varName, timeseriesDataExample.py

# read timeseries into studyVarData
for studyName in studyMap:
    varData = {}
    for dssFile in studyMap[studyName].data_src:
        print 'open data src:', dssFile

        for varName in studyMap[studyName].varPathMap:
            dssPath =  studyMap[studyName].varPathMap[varName].path
            try:
                ts = dss_retrieve_ts(dssFile,selector=dssPath,unique=True)
                print 'found  var:  '+varName+': '+dssPath
                print ts.data
                # put data into dictionary
                varData[varName]=ts.data

            except:
                # path not found in this file
                pass
 
    # put data into dictionary
    studyVarData[studyName]=varData


#W.evaluateDTS(studyVarData)