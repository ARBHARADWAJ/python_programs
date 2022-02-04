import statistics
from statistics import mode
def msce(list):
    return(mode(list))

#create a funvtion that which read all and find large number
str=[]
str1=""
str2=""
n=int(input('Enter the number of strings:'))
print("Enter the string:")
for i in range(n):
    str1=input()
    str2+=str1
print(str2)
for i in range(len(str2)):
    s=str2[i]
    str.append(s)
wss=msce(str)
print(wss)
j=str.count(wss)
#print(j)
str.remove(wss)
num=1
while num>0:
    wws=msce(str)
    wwd=str.count(wws)
    if j==wwd:
        num=1
        print(wws)
        str.remove(wws)
    else:
        num=0
    

