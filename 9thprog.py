# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:07:00 2021

@author: User
"""

n=int(input("Enter the no of elements : "))
list=[]
list2=[]
for i in range(n):
    vv=int(input("Enter the element: "))
    if(vv<=n):
      list.append(vv)
    else:
      list2.append(vv)
      print("added in list 2")
print(list)    
print(list2)    