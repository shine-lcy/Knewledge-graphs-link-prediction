def getEntityList():
    f = open("entity2id.txt","r")
    list = []
    lines = f.readlines()
    for line in lines:
        entity = line.split('\t')[0].strip()
        list.append(entity)
    return list

entitylist = getEntityList()
f1 = open("train.txt","r")
f2 = open("adjlist.txt","w")
for i in range(146916):
    a = f1.readline()
    b = a.strip().split('\t')
    en1 = b[0]
    en2 = b[1]
    en1id = entitylist.index(en1) + 1
    en2id = entitylist.index(en2) + 1
    strings = str(en1id) + ' ' + str(en2id) + '\n'
    f2.write(strings)
