# You are using Python
def pri(str,low,high):
    ss=""
    for i in range(low,high+1):
        #print(str[i],end="")
        ss+=str[i]
    return ss    

def langestpa(str):
    n=len(str)
    maxlengh=1
    start=0
    for i in range(n):
        for j in range(i,n):
            flag=1
            for k in range(0,((j-i)//2)+1):
                if(str[i+k]!=str[j-k]):
                    flag=0
            if(flag!=0 and (j-i+1)>maxlengh): 
                start=i
                maxlengh=j-i+1
    return  pri(str,start,start+maxlengh-1)
    
ma=input()
print(langestpa(ma))