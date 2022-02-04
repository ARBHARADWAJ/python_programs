# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:46:47 2021

@author: User
"""

def dayOfProgrammer(year):
    if year<1918:
        if year%4==0:
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
    elif year>1918:            
        if year%400==0 or (year%4==0 and year%100!=0):
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
    else:
        print("26.09."+str(year))
        
n=int(input())
dayOfProgrammer(n)                        
    
    
