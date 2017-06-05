from dts.Study import Study
from dts import Workflow
from dts import Debug
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections


# parse setting file and vardef files
status, studyMap = Workflow.readReference('./example_data/sample.setting')
if status!=0:  #has errors
    quit()

# this is where the timeseries stored
studyVarData = {} # studyVarData[studyName][varName]=timeseries

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
                #print ts.data
                varData[varName]=ts.data

            except:
                # dss path not found in this dss file
                pass
 
    # put data into dictionary
    studyVarData[studyName]=varData


# compute derived timeseries and then store them in studyVarData
Workflow.evaluateDTS(studyVarData)


Debug.printCSV(studyVarData)

print '...'



