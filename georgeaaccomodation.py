# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:45:05 2021

@author: User

c=0
n=int(input())
while(n>0): 
   a,b=[int(x) for x in input().split(" ")]
   if  a!=b and b-a>2 :
       c+=1
   n-=1    
print(c)       
#=>ord->"""
a='t'
b=int(ord(a))
print(b-97)
c="A"
d=int(ord(c))
print(d-64)