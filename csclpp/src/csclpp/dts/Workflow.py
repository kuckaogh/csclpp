import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import os
from antlr4.error import Err
import collections
from vtools.datastore.dss.api import *
from vtools.functions.api import *
from vtools.data.api import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


debugOn = False


def readReference(fs):
    status=0
    
    ds = os.path.dirname(fs)
    Err.errFile=fs
    P.parseSetting(fs)
    
    for s in S.studyMap:
        sty = S.studyMap[s]
        
        defaultConstMap=setDefaultConst(); sty.constMap=defaultConstMap
        
        #print sty.constMap
        varFile=sty.varFile
        
        # update data_src path
        updated_data_src=[]
        for u in sty.data_src:
            d = os.path.dirname(u)
            if d == '.' : 
                ut = os.path.join(ds,os.path.basename(u)).replace('\\', '/')
            else:
                ut = os.path.join(ds,d,os.path.basename(u)).replace('\\', '/')
            updated_data_src.append(str(ut))
        sty.data_src = updated_data_src
        #print updated_data_src

        vf=''
        vd = os.path.dirname(varFile)
        if vd == '.' : 
            vf = os.path.join(ds,os.path.basename(varFile)).replace('\\', '/')
        else:
            vf = os.path.join(ds,d,os.path.basename(varFile)).replace('\\', '/')
                        
        
        #print vf
        Err.errFile=vf
        varDef, varPathGroupMap, tempVarGroupList, ifsMapGroupMap, \
        strArrayGroupMap, intArrayGroupMap, floatArrayGroupMap, constGroupMap=P.parseVarDef(vf, defaultConstMap)

        #print 'intArrayGroupMap', intArrayGroupMap
        
        sty.varDef = varDef
        sty.varPathMap=varPathGroupMap[varDef]

        sty.tempVarList = tempVarGroupList[varDef]
        sty.ifsMap = ifsMapGroupMap[varDef]

        sty.strArrayMap.update(strArrayGroupMap[varDef])
        sty.intArrayMap.update(intArrayGroupMap[varDef])        
        sty.floatArrayMap.update(floatArrayGroupMap[varDef]) 
        sty.constMap.update(constGroupMap[varDef])
        
        #print 'sty.constMap', sty.constMap
        
        # process metadata dictionary type
        _cm=sty.constMap
        #print '_cm:', _cm
        for k, v in sty.varPathMap.iteritems():
            for e in v.metaDataPost:
                #print k, v.metaData[e]
                _dummy={}
                es = '_dummy='+v.metaData[e]
                #print 'es:',es
                exec(es)
                #print _dummy
                v.metaData[e]=_dummy
                
                
                
    
    status = len(Err.errors) 
    if status !=0: quit()  
    return S.studyMap



def evaluateDTS(studyVarTs):

    for s in studyVarTs:
        if not S.studyMap[s].ifsMap: return
        #global _ts
        es=''
        _ts = studyVarTs[s]
        #print s, '_ts.keys():', _ts.keys()

        iend=len(_ts.values()[0])

        needTag=False
        #es=es+'for i in range(0,'+str(iend)+'):\n'   
        for p in S.studyMap[s].ifsMap:
            ifs = S.studyMap[s].ifsMap[p]
            #print 'if statement ID: '+ str(p)
                
            for idx, condition in enumerate(ifs):                
                #print condition
                if condition[0]=='!':
                    es=es+'for i in range(0,'+str(iend)+'):\n' 
                    es=es+'\t'+condition[1:]+'\n'
                    #es=es+condition[1:]+'+0\n'
                    needTag=True
                    continue
                else:
                    if needTag:
                        #es=es+'for i in range(0,'+str(iend)+'):\n'   
                        needTag=False                        
                        
                if idx<1:
                    es=es+'for i in range(0,'+str(iend)+'):\n' 
                    es =es + '\tif ' + condition + ":\n"
                    for a in ifs[condition]:
                        es = es + '\t\t'+a+'\n'
                else:
                    if condition=='always':
                        es =es + '\telse:\n'
                    else:
                        es =es + '\telif ' + condition + ":\n"
                    for a in ifs[condition]:
                        es = es + '\t\t'+a+'\n'                   
            es =es+'\n'
    
        if debugOn:
            text_file = open(s+"_es_printout.py", "w")
            text_file.write(es)
            text_file.close()
        Err.errFile = 'If statement evaluation'
        
#         for k,v in S.studyMap[s].constMap.iteritems():
#             #print k, v.const
#             _ts[k]=v.const
        exec(es, {'_ts':_ts}) 
#         for k in S.studyMap[s].constMap.keys():
#             _ts.pop(k, None)

#         import timeit
#         start_time = timeit.default_timer()
#         for w in range(0,1000):
#             exec(es, {'_ts':_ts}) 
#         print(timeit.default_timer() - start_time)
  
         
    
def evaluateIFS0(studyVarTs):
    es=''
    results={}
    for s in studyVarTs:
        ts = studyVarTs[s]
        new = {}
        #for studyVarTs[s].
        print ts
        es=es+'locals().update(ts)\n'
        es=es+'print D418\n'
        for p in S.studyMap[s].ifsMap:
            ifs = S.studyMap[s].ifsMap[p]
            #print 'if statement ID: '+ str(p)
            for idx, condition in enumerate(ifs):
                if idx<1:
                    es =es + 'if ' + condition + ":\n"
                    for a in ifs[condition]:
                        es = es + '    '+a+'\n'
                else:
                    if condition=='always':
                        es =es + 'else:\n'
                    else:
                        es =es + 'elif ' + condition + ":\n"
                    for a in ifs[condition]:
                        es = es + '    '+a+'\n'                   
            es =es+'\n'
        
    print es
    text_file = open("es.py", "w")
    text_file.write(es)
    text_file.close()
    #exec("if 3> 1: print 'yes'")
    exec(es)


        
def test_evaluateDTS(studyVarTs):
    
    #T.styVarTs=studyVarTs
    
    for s in studyVarTs:
        varTs = studyVarTs[s]
        
        k = varTs['s_folsom'] + varTs['s_shasta']
        print 'fol:', varTs['s_folsom']
        print 'sha:', varTs['s_shasta']
        print '+:  ', k 
        print '/:  ', varTs['s_folsom'] / varTs['s_shasta']
        print '*:  ', varTs['s_folsom'] * varTs['s_shasta']        
        
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
# read timeseries into studyVarData  
def readData(studyMap, time_window=None):
    studyVarData = collections.OrderedDict();
    
    for studyName, styV in studyMap.iteritems():

        missingVars = styV.varPathMap.keys()
        start_earliest=datetime(2900,1,1,0,0)
        end_latest=datetime(500,1,1,0,0)
        varData = collections.OrderedDict();
        varData['datetime']=None
        varData['year']=None
        varData['month']=None
        varData['daysin']=None

        iend=0
        for dssFile in styV.data_src:
            print 'open data src:', dssFile
    
            for varName, var in styV.varPathMap.iteritems():
                dssPath =  var.path
                try:
                    ts = dss_retrieve_ts(dssFile,selector=dssPath,time_window=time_window,unique=True)
                    if varName in varData.keys():
                        Err.addError('This var exists in multiple DSS files: '+varName+':'+dssPath, '', '')
                    print 'found  var:  '+varName+': '+dssPath
                    #print ts.data
                    varData[varName]=ts.data
                    var.metaData['_unit']=ts.props['unit']
                    #find length
                    if len(ts.data)> iend: iend = len(ts.data)
                    if ts.start<start_earliest: start_earliest=ts.start
                    if ts.end>    end_latest: end_latest= ts.end
                        
                    var.metaData['_start']=ts.start  
                    var.metaData['_end']=ts.end    
                    
                    missingVars.remove(varName)
                    
                except:
                    #print varName+':'+dssPath+' not found.'# dss path not found in this dss file
                    pass
            
        # check missing vars
        if missingVars:
            Err.addError('These vars not found in DSS files: '+str(missingVars), '', '')
                
            
        # reserve space for new vars
        arrayN=diff_month(end_latest,start_earliest)+1
        #print 'arrayN:', arrayN
        #print 'arrayN', arrayN

            
        for varName,v in styV.strArrayMap.iteritems():
            vd=np.empty(arrayN)
            vd=vd.astype(np.str)
            vd.fill('')
            varData[varName]=vd
        for varName,v in styV.intArrayMap.iteritems():
            vd=np.empty(arrayN)
            vd=vd.astype(np.int)
            vd.fill(0)
            varData[varName]=vd
        for varName,v in styV.floatArrayMap.iteritems():
            vd=np.empty(arrayN)
            vd=vd.astype(np.float)
            vd.fill(0)
            varData[varName]=vd
            
        # attach datetime
        dtName='datetime'
        dtv=Var('')
        dtv.metaData['_dataType']='datetime'
        styV.varSystemMap[dtName]=dtv
        varData[dtName]=start_earliest + np.arange(arrayN) * relativedelta(months=1)
        
        dtName='year'
        varData[dtName]= (start_earliest.year+ np.floor((np.arange(arrayN)+start_earliest.month-1)/12).astype(np.int))
        
        dtName='month'      
        varData[dtName]= np.mod(start_earliest.month+np.arange(arrayN)-1,12)+1            


        dtName='daysin'
        import calendar
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        vd=np.empty(arrayN);vd=vd.astype(np.int)
        varData[dtName]=vd
        styV.tempVarList.append(dtName)
        for i in range(arrayN):
            y= varData['year'][i]
            m = varData['month'][i]
            if m!=2:
                varData[dtName][i]=month_days[m]
            else:
                if not calendar.isleap(y):
                    varData[dtName][i]=month_days[m]
                else:
                    varData[dtName][i]=29
            
            
            
                  
        
            
        #print 'month', varData['month']
        # put data into dictionary
        studyVarData[studyName]=varData
        
        studyMap[studyName].start_earliest=start_earliest
        studyMap[studyName].end_latest=end_latest


        # fill nan 
        if time_window==None:        
            
            #print styV.start_earliest, styV.end_latest
            for k,v in styV.varPathMap.iteritems():
                #print k, v.metaData['_start'], v.metaData['_end']
                #print k, diff_month(v.metaData['_start'],styV.start_earliest), diff_month(styV.end_latest, v.metaData['_end'])
                pre_n=diff_month(v.metaData['_start'],styV.start_earliest)
                post_n=diff_month(styV.end_latest, v.metaData['_end'])
                
                if pre_n>0:
                    pre=np.empty(pre_n); pre.fill(np.nan)
                    varData[k] = np.concatenate((pre, varData[k]))
                
                if post_n>0:
                    post=np.empty(post_n); post.fill(np.nan)
                    varData[k] = np.concatenate((varData[k],post))
                                    
    return studyVarData   


def setDefaultConst():
    
    d=collections.OrderedDict();
    l=[('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)]
    for k in l:
        v=Var('')
        v.metaData['_dataType']=np.int
        v.const=k[1]
        d[k[0]]=v
  
    return d
    
#     d['jan']=1; d['feb']=2; d['mar']=3; d['apr']=4; d['may']=5; d['jun']=6
#     d['jul']=7; d['aug']=8; d['sep']=9; d['oct']=10; d['nov']=11; d['dec']=12      
    
