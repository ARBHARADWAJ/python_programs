# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:23:42 2021

@author: User
"""
"""i want to do the file program to make a beautiful program to take the input values for an employee and save it in file and save the program"""
print("1.read the file \n2.write the file")
if((int(input("Enter the option: ")))==2):
    fln=input("Enter the file name: ")
    fs=open(fln,"w")
    if(fs.write(input("Enter the message:"))):
        print("completed saving")
else:
    fln=input("Enter the file name: ")
    fs=open(fln,"r")
    print(fs.read(),"\ndone!..")

"""fln=input("Enter the file name: ")
fs=open(fln,"r+")
if(fs.write(input("Enter the message:"))):
   print("completed saving")
print(fs.read())
   """