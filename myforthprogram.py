l=input().split()
l.sort()
if(l[0]==l[1]):
    d=int(l[2])
else:
    d=int(l[1])
#print(l[1])
#l=l.reverse()
if(l[len(l)-1]>l[len(l)-2]):
    c=int(l[len(l)-2])
else:
    c=int(l[len(l)-3])
#d=int(l[1])
sum=c+d
print(int(sum))