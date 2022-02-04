# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:34:20 2021

@author: User
"""

lll=[]
lis=input("Enter the name: \t")
for i in range(len(lis)):
    if (lis[i]>='a' and lis[i]<='z')or(lis[i]>='A' and lis[i]<='Z'):
      print(lis[i],"\t")
lll=lis
sorted(lll)
for i in range(len(lll)):
    if (lll[i]>='1' and lll[i]<='9'):
      print(lll[i])

