# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:48:48 2021

@author: User
"""

for _ in range(int(input())):
    n=int(input())
    inp=[int(i) for i in input().split()]
    b=[(inp[i],i) for i in range(n)]
    b.sort()
    a=[0]*n
    w=0
    for bi,i in b:
        if w<=bi-1:
            a[i]=w
            w=w+1
        else:
            a[i]=0
    print(*a)       
            