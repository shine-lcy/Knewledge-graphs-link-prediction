import numpy as np
import time
EntityVector = np.loadtxt('entity2vec_wanzheng.txt')
RelationVector = np.loadtxt('relation2vec_m=2n=200.txt')

def getEntityList()
    f = open(entity2id.txt,r)
    list = []
    lines = f.readlines()
    for line in lines
        entity = line.split('t')[0].strip()
        list.append(entity)
    return list

def getRelationList()
    f = open(relation2id.txt,r)
    list = []
    lines = f.readlines()
    for line in lines
        relation = line.split('t')[0].strip()
        list.append(relation)
    return list

def getEntityClassList()
    f = open(entityclass.txt,r)
    list = []
    lines = f.readlines()
    for line in lines
        classnumber = line.strip()
        list.append(classnumber)
    return list

def getAlreadyTailList()
    f = open(alreadytail.txt,r)
    list1 = []
    lines = f.readlines()
    for line in lines
        list2 = []
        line = line.strip()
        a = line.split('t')
        for b in a
            list2.append(b)
        list1.append(list2)
    return list1


def getAlreadytailList(head,relation)
    f = open(train.txt,r)
    list = []
    lines = f.readlines()
    for line in lines
        nowhead = line.split('t')[0].strip()
        nowrelation = line.split('t')[2].strip()
        nowtail = line.split('t')[1].strip()
        if (head==nowhead) and (relation==nowrelation)
            list.append(nowtail)
    return list

def getTailClass(relation)
    if (relation==author_is_in_field)
        classnumber = 2
    elif (relation==field_is_part_of)
        classnumber = 2
    elif (relation==work_in)
        classnumber = 4
    elif (relation==paper_cit_paper)
        classnumber = 1
    elif (relation==paper_is_in_field)
        classnumber = 2
    elif (relation==paper_is_written_by)
        classnumber = 0
    elif (relation==paper_publish_on)
        classnumber = 3
    return classnumber

f1 = open(testorig.txt,r)
f2 = open(test_submit_v10.txt,w)
line = f1.readline()
entitylist = getEntityList()
relationlist = getRelationList()
entityclasslist = getEntityClassList()
alreadytaillist = getAlreadyTailList()
start = time.time()
for i in range(11529)
    if (i%100==0)
        end = time.time()
        print (str(i)+'t'+str(end-start))
        start = time.time()
    a = f1.readline()
    b = a.split(',')
    head = b[1].strip()
    relation = b[2].strip()
    neededtailclass = getTailClass(relation)
    headid = entitylist.index(head)
    relationid = relationlist.index(relation)
    hdAdRln = EntityVector[headid,] + RelationVector[relationid,]
    entity_dict = {}
    for j in range(17313)
        dist = np.linalg.norm(EntityVector[j,] - hdAdRln, ord = 1)
        entity_dict[j] = dist
    sort_dict = sorted(entity_dict.items(),key=lambda itemitem[1])
    resultlist = []
    n = 0
    while (len(resultlist)3)
        tailid = entitylist.index(entitylist[sort_dict[n][0]])
        tailclass = int(entityclasslist[tailid])
        if (tailclass==neededtailclass)
            if (entitylist[sort_dict[n][0]] not in alreadytaillist[i])
                resultlist.append(entitylist[sort_dict[n][0]])
        n += 1
    result_entity = str(resultlist[0])+ +resultlist[1]+ +resultlist[2]+'n'
    f2.write(result_entity)