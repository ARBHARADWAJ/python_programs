n,h=[int(x) for x in input().split()]
b=0

x = [int(x) for x in input().split(" ")]    
for i in range(len(x)):     
    if x[i]>h:
        b+=2
    else:
        b+=1
    n=n-1
print(b)
