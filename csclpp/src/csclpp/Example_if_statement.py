import sys
import dts.Parser as P
from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
from dts import Workflow
from dts import Debug
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections
import csv

studyMap = Workflow.readReference('./example_data/if_statement.setting')
    

# this is where the timeseries stored
studyVarData = {} # studyVarData[studyName][varName]=timeseries

# read timeseries into studyVarData
for studyName in studyMap:
    varData = collections.OrderedDict();
    iend=0
    for dssFile in studyMap[studyName].data_src:
        print 'open data src:', dssFile

        for varName in studyMap[studyName].varPathMap:
            dssPath =  studyMap[studyName].varPathMap[varName].path
            try:
                ts = dss_retrieve_ts(dssFile,selector=dssPath,unique=True)
                print 'found  var:  '+varName+': '+dssPath
                #print ts.data
                varData[varName]=ts.data
                
                #find length
                if not iend:
                    iend = len(ts.data)
            except:
                # dss path not found in this dss file
                pass
        
        # reserve space for new vars
        for varName in studyMap[studyName].newArrayMap:
            varData[varName]=[0]*iend
          
    # put data into dictionary
    studyVarData[studyName]=varData


# compute derived timeseries and then store them in studyVarData
Workflow.evaluateDTS(studyVarData)


# evaluate If Statements
Workflow.evaluateIFS(studyVarData)


#print csv
for s, d in studyVarData.iteritems():

    with open(s+".csv", "wb") as outfile:
        w = csv.writer(outfile)
        w.writerow(d.keys())
        w.writerows(zip(*d.values()))  
    outfile.close() 

print __file__

