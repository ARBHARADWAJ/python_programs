aga=[]
target=int(9)
v=[]
def backtrack(A,st,v,v1):
    if(sum(v1)==9): 
       v.append(v1)
       aga.append(v1)
   # print(v1," ",v)
    for i in range(st,len(A)):
        v1.append(A[i])
       # print(A[i])
        backtrack(A,i+1,v,v1)

        v1.pop()

A=[1,2,3]
sorted(A)
#[[]]#v
#[]#v1

backtrack(A,0,[],[])
print(v)
print(aga)
