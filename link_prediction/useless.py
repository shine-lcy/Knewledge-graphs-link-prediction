f1 = open("test_submit_v2.txt","r")
f2 = open("test_submit_v3.txt","w")
lines = f1.readlines()
for line in lines:
    a = line.strip()
    b = len(a)
    c = a[b-26:b]
    f2.write(c+'\n')