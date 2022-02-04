#n=int(input())
l=[];
#for i in range(n):
#    ss=int(input())
#    l.append(ss)
l=input().split()    

aa=[];
for s in l:
    if s not in aa:
        aa.append(int(s))
aa.sort()
s1=aa[1]
s2=aa[len(aa)-2]
print(s1+s2) 