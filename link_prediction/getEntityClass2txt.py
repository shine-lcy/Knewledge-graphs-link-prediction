def getEntityList():
    f = open("entity2id.txt","r")
    list = []
    lines = f.readlines()
    for line in lines:
        entity = line.split('\t')[0].strip()
        list.append(entity)
    return list

def getHeadClass(relation):
    if (relation=="author_is_in_field"):
        classnumber = 0
    elif (relation=="field_is_part_of"):
        classnumber = 2
    elif (relation=="work_in"):
        classnumber = 0
    elif (relation=="paper_cit_paper"):
        classnumber = 1
    elif (relation=="paper_is_in_field"):
        classnumber = 1
    elif (relation=="paper_is_written_by"):
        classnumber = 1
    elif (relation=="paper_publish_on"):
        classnumber = 1
    return classnumber

def getTailClass(relation):
    if (relation=="author_is_in_field"):
        classnumber = 2
    elif (relation=="field_is_part_of"):
        classnumber = 2
    elif (relation=="work_in"):
        classnumber = 4
    elif (relation=="paper_cit_paper"):
        classnumber = 1
    elif (relation=="paper_is_in_field"):
        classnumber = 2
    elif (relation=="paper_is_written_by"):
        classnumber = 0
    elif (relation=="paper_publish_on"):
        classnumber = 3
    return classnumber



f1 = open("train.txt","r")
entitylist = getEntityList()
lines = f1.readlines()
entityclasslist = [0 for i in range(17313)]
for line in lines:
    contents = line.split('\t')
    head = contents[0].strip()
    tail = contents[1].strip()
    relation = contents[2].strip()
    headclass = getHeadClass(relation)
    tailclass = getTailClass(relation)
    headid = entitylist.index(head)
    tailid = entitylist.index(tail)
    entityclasslist[headid] = headclass
    entityclasslist[tailid] = tailclass

f2 = open("entityclass.txt","w")
for item in entityclasslist:
    f2.write(str(item)+"\n")
