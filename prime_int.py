n=int(244234933)
br=True
for i in range(2,n):
    if(n%i==0):
        br=False
        break
if(br==False):
    print("no")
else:
    print("Tru")    

