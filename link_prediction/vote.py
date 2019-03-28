

dic = {}
f1 = open("test_submit_v9.txt","r")
f2 = open("test_submit_v8.txt","r")
f3 = open("test_submit_v7.txt","r")
f4 = open("test_submit_v5.txt","r")
f5 = open("test_submit_v10.txt","r")
f6 = open("results_wcy1.txt","r")
f7 = open("results_wcy2.txt","r")
f8 = open("test_submit_v11.txt","r")
f9 = open("results_wcy3.txt","r")
fw = open("test_submit_vote_9.txt","w")
for i in range(11529):
    a1 = f1.readline()
    b1 = a1.strip().split(' ')
    for item in b1:
        if (item in dic.keys()):
            dic[item] += 0.248
        else:
            dic[item] = 0.248
    a2 = f2.readline()
    b2 = a2.strip().split(' ')
    for item in b2:
        if (item in dic.keys()):
            dic[item] += 0.235
        else:
            dic[item] = 0.235
    a3 = f3.readline()
    b3 = a3.strip().split(' ')
    for item in b3:
        if (item in dic.keys()):
            dic[item] += 0.21
        else:
            dic[item] = 0.21
    a4 = f4.readline()
    b4 = a4.strip().split(' ')
    for item in b4:
        if (item in dic.keys()):
            dic[item] += 0.21
        else:
            dic[item] = 0.21
    a5 = f5.readline()
    b5 = a5.strip().split(' ')
    for item in b5:
        if (item in dic.keys()):
            dic[item] += 0.266
        else:
            dic[item] = 0.266
    a6 = f6.readline()
    b6 = a6.strip().split(' ')
    for item in b6:
        if (item in dic.keys()):
            dic[item] += 0.28
        else:
            dic[item] = 0.28
    a7 = f7.readline()
    b7 = a7.strip().split(' ')
    for item in b7:
        if (item in dic.keys()):
            dic[item] += 0.28
        else:
            dic[item] = 0.28
    a8 = f8.readline()
    b8 = a8.strip().split(' ')
    for item in b8:
        if (item in dic.keys()):
            dic[item] += 0.202
        else:
            dic[item] = 0.202
    a9 = f9.readline()
    b9 = a9.strip().split(' ')
    for item in b9:
        if (item in dic.keys()):
            dic[item] += 0.36
        else:
            dic[item] = 0.36
    # b = b1+b2+b5+b6+b7
    # num = -1
    # for item in b:
    #     num += 1
    #     num = num % 3
    #     score = 3 - num
    #     if (item in dic.keys()):
    #         dic[item] += score
    #     else:
    #         dic[item] = score
    # print (dic)
    # for item in b:
    #     if (item in dic.keys()):
    #         dic[item] += 1
    #     else:
    #         dic[item] = 1
    c = sorted(dic.items(), key=lambda item:item[1], reverse=True)
    resultlist = []
    for j in range(3):
        resultlist.append(c[j][0])
    result_entity = str(resultlist[0]) + " " + resultlist[1] + " " + resultlist[2]
    if (i<11528):
        result_entity = result_entity + '\n'
    fw.write(result_entity)
    dic = {}
