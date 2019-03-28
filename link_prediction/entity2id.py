f1 = open("trainorig.txt","r")
f2 = open("entity2id2.txt","w")
a = f1.readline()
num = 0
entitylist = []
for i in range(146916):
    a = f1.readline()
    b = a.split(',')
    if (b[1] == 'author_is_in_field'):
        c1 = b[0].strip()
        if c1 not in entitylist:
            entitylist.append(c1)
        c2 = b[2].strip()
        if c2 not in entitylist:
            entitylist.append(c2)

for item in entitylist:
    f2.write(item+'\t'+str(num)+'\n')
    num += 1
print (num)
