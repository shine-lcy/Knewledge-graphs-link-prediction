f1 = open("trainorig.txt","r")
f2 = open("relation2id.txt","w")
a = f1.readline()
num = 0
relationlist = []
for i in range(146916):
    a = f1.readline()
    b = a.split(',')
    c = b[1].strip()
    if c not in relationlist:
        relationlist.append(c)
for item in relationlist:
    f2.write(item+'\t'+str(num)+'\n')
    num += 1
print (num)
