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


debugOn = True


def readReference(fs):
    status=0
    
    ds = os.path.dirname(fs)
    Err.errFile=fs
    P.parseSetting(fs)
    
    for s in S.studyMap:
        sty = S.studyMap[s]
        varFile=sty.varFile
        #varDef =sty.varDef
        #print varFile, varDef
        
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
        
        
        vf=os.path.join(ds,varFile+'.vardef').replace('\\', '/')
        Err.errFile=vf
        varDef, varPathGroupMap, varExprGroupMap, tempVarGroupList, ifsMapGroupMap, \
        newArrayGroupMap, newConstGroupMap=P.parseVarDef(vf)
#         S.fileVarPathGroupMap[varFile]=T.varPathGroupMap
#         S.fileVarExprGroupMap[varFile]=T.varExprGroupMap
        sty.varDef = varDef
        sty.varPathMap=varPathGroupMap[varDef]
        sty.varExprMap=varExprGroupMap[varDef]
        sty.tempVarList = tempVarGroupList[varDef]
        sty.ifsMap = ifsMapGroupMap[varDef]
        sty.newArrayMap = newArrayGroupMap[varDef]
        sty.newConstMap = newConstGroupMap[varDef]
        
        
        # process metadata dictionary type
        for k, v in sty.varPathMap.iteritems():
            for e in v.metaDataPost:
                print k, v.metaData[e]
                
                
                
    
    status = len(Err.errors) 
    if status !=0: quit()  
    return S.studyMap
#     for s in S.studyMap:
#         sty = S.studyMap[s]
#         for k in sty.varMap:
#             v=sty.varMap[k]
#             print k, v.isTemp, v.path, v.expr

        
def evaluateDTS(studyVarTs):
    
    #T.styVarTs=studyVarTs
    
    for s in studyVarTs:
        #T.varTs = T.styVarTs[s]
        
        eList=[]
        for vk in S.studyMap[s].varExprMap:
            e = S.studyMap[s].varExprMap[vk].expr+'+0'
            if e: eList.append(vk+'='+e+'\n')
        
        line = ''.join(eList)
        if line: 
            #print line
            Err.errFile = line
            P.evaluateDTS(studyVarTs[s], line)    
        
        #print T.styVarTs[s]
        
        
#         for var in T.styVarTs[s]:
#             print var, T.styVarTs[s][var]

def evaluateIFS(studyVarTs):
    es=''
    results={}
    for s in studyVarTs:
        if not S.studyMap[s].ifsMap: return
        global _ts
        _ts = studyVarTs[s]
        #print ts
        #es=es+'print globals()\n'
        iend=len(_ts.values()[0])
        es=es+'for i in range(0,'+str(iend)+'):\n'
        for p in S.studyMap[s].ifsMap:
            ifs = S.studyMap[s].ifsMap[p]
            #print 'if statement ID: '+ str(p)
            for idx, condition in enumerate(ifs):
                if idx<1:
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
        text_file = open("es_printout.py", "w")
        text_file.write(es)
        text_file.close()
    Err.errFile = 'If statement evaluation'
    exec(es, {'_ts':_ts})    
    
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
        

# read timeseries into studyVarData  
def readData(studyMap):
    studyVarData = collections.OrderedDict();

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
    return studyVarData   
