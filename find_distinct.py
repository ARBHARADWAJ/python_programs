# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:20:23 2021

@author: User
"""
def ppp(x):
    str=""
    for i in x:
        str=str+i
    print(str)    


n=int(input())
while n>0:
    string1=input()
    string2=input()
    x=[]
    for i in string2:
        if (i  not in string1) and (i not in x):
            x.append(i)
    x.sort()
    ppp(x)        
        
    
    
    n=n-1