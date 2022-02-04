# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:13:11 2021

@author: User
"""
n=int(input())
arr=[int(x) for x in input().split()]
q=int(input())
for i in range(q):
    a,b=input().split()
    #print(a," ",b)
    c=int(a)
    d=int(b)
    arr2=arr[c:d+1]
    print(sum(arr2))

#arr2=[]
"""10
1 30 13 -4 -5 12 -53 -12 43 100 
4
0 5
1 7
2 3
7 9
"""
#print(sum(arr2))