def getAlreadytailList(head,relation):
    f = open("train.txt","r")
    list = []
    lines = f.readlines()
    for line in lines:
        nowhead = line.split('\t')[0].strip()
        nowrelation = line.split('\t')[2].strip()
        nowtail = line.split('\t')[1].strip()
        if (head==nowhead) and (relation==nowrelation):
            list.append(nowtail)
    return list

import time
f1 = open("testorig.txt","r")
f2 = open("alreadytail.txt","w")
line = f1.readline()
start = time.time()
for i in range(11529):
    if (i%100==0):
        end = time.time()
        print (str(i)+'\t'+str(end-start))
        start = time.time()
    a = f1.readline()
    b = a.split(',')
    head = b[1].strip()
    relation = b[2].strip()
    alreadytaillist = getAlreadytailList(head,relation)
    alreadytaillist.append(head)
    for item in alreadytaillist:
        f2.write(item+'\t')
    f2.write('\n')
