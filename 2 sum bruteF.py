lis=[2,7,5,8]#range of 2 frames so that it is easy to form else it would form a problem
target=int(9)
list=[]
list1=[]
for i in range(len(lis)):
    for j in range(1,len(lis)):
        if lis[i]+lis[j]==target:
            list.append(i)
            list.append(j)
            list1.append(list)


print(list1)
