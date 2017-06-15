from dts.Study import Study
from dts import Workflow
from dts import Debug
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections
import csv


# parse setting file and vardef files
studyMap = Workflow.readReference('./example_data/if_statement.setting')
    

# read timeseries into studyVarData  
studyVarData = Workflow.readData(studyMap)


# compute derived timeseries and then store them in studyVarData
print 'evaluateDTS'
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

