# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:17:56 2021

@author: User
"""


#program that elemenates the -4 4 and remindered value 4 and print remaining:

l=[]    
l=input().split()
for i in range(len(l)):
   l[i]=int(l[i])
   if (int(l[i])%10!=4) and l[i]!=-4: 
      print (l[i],end=" ")
   else:
       if l[i]==0:
           print(l[i],end=" ")
           
            
# print (l[i],end=" ")
#23 -4 8 9 -7 1   23 -4 8 9 -7 1
""""if l[i]<0 or l[i]==0 and l[i]!=-4 :
       print (l[i],end=" ")
   else:
       if(int(l[i])%10!=4):
            print (l[i],end=" ")
  
     elif l[i]!=-4:
     print(l[i],end=" ") """ 
  
    