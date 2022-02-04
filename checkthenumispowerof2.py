# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:23:53 2021

@author: User
"""
def find_num_pow_2(n):
    if n==0:
        return 0
    while (n!=1):
          if (n%2!=0):
              return 0
          n=n//2
    return 1      
    
    
    
num=int(input())
while num>0:
    num=num-1
    n=int(input())
    if(find_num_pow_2(n)):
        print("True")
    else:
        print("False")   
    