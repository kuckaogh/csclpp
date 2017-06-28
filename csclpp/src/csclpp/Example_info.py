from dts.Study import Study
from dts.Var import Var
import dts.Setting as S
import dts.Workflow as W
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
import collections
from dts import Workflow

#studyMap = W.readReference('./example_data/easy.setting')
studyMap = W.readReference('./example_data/if_statement.setting')

# read timeseries into studyVarData  
studyVarData = Workflow.readData(studyMap, time_window='(9/15/1921 00:00,1/15/1922 00:00)')


# take a look at the var maps

for k, sv in studyMap.iteritems():
    
    print '\nstudyName:', k, ' vardef:', sv.varDef
    for d in studyMap[k].data_src:
        print 'dss data src:', d
        
    print ''
    for p, v in studyMap[k].varPathMap.iteritems():
        print '  var:  '+p+'= '+v.path
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost
    

    print ''
    for p, v in studyMap[k].floatArrayMap.iteritems():
        print '  float array:  '+p
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost

    print ''
    for p, v in studyMap[k].intArrayMap.iteritems():
        print '  int array:  '+p
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost

    print ''
    for p, v in studyMap[k].strArrayMap.iteritems():
        print '  string array:  '+p
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost

    print ''
    for p, v in studyMap[k].constMap.iteritems():
        print '  const:  '+p+'= ', v.const
        if v.metaData: 
            print v.metaData   #print units, capacity
        if v.metaDataPost:
            print v.metaDataPost
            
    print ''
    print '  temp vars:', studyMap[k].tempVarList
