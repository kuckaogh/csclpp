from Study import Study
import Workflow
import Debug
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections
import csv


# parse setting file and vardef files
studyMap = Workflow.readReference('./example_data/easy.setting')


# read timeseries into studyVarData  
studyVarData = Workflow.readData(studyMap)


# compute derived timeseries and then store them in studyVarData
print 'evaluateDTS'
Workflow.evaluateDTS(studyVarData)


#print csv
for s, d in studyVarData.iteritems():
    #print d.values
    with open(s+".csv", "wb") as outfile:
        w = csv.writer(outfile)
        w.writerow(d.keys())
        w.writerows(zip(*d.values()))  
    outfile.close() 

print __file__

