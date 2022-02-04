# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:09:42 2021

@author: User
"""
n=int(input())
xm=[int(x) for x in input().split()]
mn=int(input())
y=[int(x) for x in input().split()]
for i in xm:
    y.remove(i)
y.sort()
y = list(dict.fromkeys(y))
for i in y:    
   print(i,end=" ")    