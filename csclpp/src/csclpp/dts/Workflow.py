import sys
import Parser as P
from Study import Study
from Var import Var
import Setting as S
import os

def readReference(fs):
    
    ds = os.path.dirname(fs)
    
    P.parseSetting(fs)
    
    for s in S.studyMap:
        sty = S.studyMap[s]
        varFile=sty.varFile
        varDef =sty.varDef
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
        
        
        vf=os.path.join(ds,varFile+'.vardef')
        varPathGroupMap, varExprGroupMap, tempVarGroupList, ifsMapGroupMap, newArrayGroupList, =P.parseVarDef(vf)
#         S.fileVarPathGroupMap[varFile]=T.varPathGroupMap
#         S.fileVarExprGroupMap[varFile]=T.varExprGroupMap
        sty.varPathMap=varPathGroupMap[varDef]
        sty.varExprMap=varExprGroupMap[varDef]
        sty.tempVarList = tempVarGroupList[varDef]
        sty.ifsMap = ifsMapGroupMap[varDef]
        sty.newArrayList = newArrayGroupList[varDef]
        
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
            e = S.studyMap[s].varExprMap[vk].expr
            if e: eList.append(vk+'='+e+'\n')
        
        line = ''.join(eList)
        if line: P.evaluateDTS(studyVarTs[s], line)    
        
        #print T.styVarTs[s]
        
        
#         for var in T.styVarTs[s]:
#             print var, T.styVarTs[s][var]

def evaluateIFS(studyVarTs):
    es=''
    results={}
    for s in studyVarTs:
        ts = studyVarTs[s]
        print ts

        for p in S.studyMap[s].ifsMap:
            ifs = S.studyMap[s].ifsMap[p]
            es=es+'if statement ID: '+ str(p)+'\n'
            for idx, condition in enumerate(ifs):
                es=es+condition+':\n'  
                for a in ifs[condition]:
                        es = es +a+'\n'               
            es =es+'\n'
        
    text_file = open("es_printout.txt", "w")
    text_file.write(es)
    text_file.close()

    
def evaluateIFS0(studyVarTs):
    es=''
    results={}
    for s in studyVarTs:
        ts = studyVarTs[s]
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
        
        
        
        
#         for var in T.styVarTs[s]:
#             print var, T.styVarTs[s][var]
    
            
        