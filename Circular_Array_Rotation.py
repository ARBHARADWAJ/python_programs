"""n,k,q=input().split()
num=[int(i) for i in input().split()]
dm=[]
q=int(q)
for i in range(q):
    aa=input()
    dm.append(aa)
#print(num,"\n",k,"\n",dm)    
num=[1,2,3,4,5]
a=num.pop(0)
print(num)
num.append(a)
print(num)"""
def rotate(a,k):
    for i in range(k):
        aa=a.pop()
        a.insert(0,aa)
    return a    

n,k,q=input().split();
num=[int(i) for i in input().split()]
kq=int(k)
asa=[]
for i in range(int(q)):
    asa.append(int(input()))
#ortation
aaa=[]
aaa=rotate(num,kq)    
for i in asa:
    print(aaa[i])