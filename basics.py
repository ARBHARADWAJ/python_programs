# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:18:06 2021

@author: User
"""

a=12321321214324241232143243422
print(a)#//no limitation for the variable 
_a='kalki'
print(_a)
_='kalki'#it can accept but the number only cant be the variable name so it 
#forms an error
print(_)
b='dfdfdf'
ss="dsdsdsd"
print(b,ss)
#conditionalstatements  ":" if we typed in the #
#line and clicked enter then we get autimatically the next ine with 4 whitespaces
# a=10  it is wrong   
#a=10   it is right,in intendation is four spaces it will be given
#if conditionalstatements:
"""age=int(input())
if age>=18:
   print("right tp vote")  
else:
    print("growup")
"""
#even or odd:
"""    
i=int(input())
if i%2==0:
    print("even");
else:
    print("odd")

year=int(input())
if  year%4==0 and year%400==0:
    if year%100!=0:
        print(year," is leap year")
else:
    print("not leap")        
#if the prog find sthe error then it founds theettots
#leap year %4==0 and i;jo 
   """ 

#.............................................................
_=32
print(_)
#but _0 is prohibitted,and we cant use number to start the variable name,it shows errror
l1=[]#;lizt
s1=()#tupple
s2={}
s3={}#dictionary
s4={1,2,3}#//set will be diifferentiated by the dta in the lsit
print(type(l1),type(s1),type(s2),type(s3),type(s4))
#...........................................
a=10
b=20
print((a//b),(a/b))
#single slash / will give the float and double slash // will give the integer.
#0 0.5
#...........................................
#arthimatical,relational,logical,bitwise
# & | ~ ^ >>(ls) <<(rs) xor=>(x&y)-(x|y)
#firts left shift
"""
10<<3-l.shift
binary equivalent -1010
add 3 zero on the right side 1010000=16+64=80
"""
print(10<<3)
print(21<<4)##left shift  10101 0000 = 336
#right shift>>   delete the zeros from right to left how many bits we have
print(21>>4)#10101-0000 from right to left that is 1

print(42>>5)#101010 -00000=> op 1 
"""
a^b=(a&b)-(a|b)
that is 1010^0101=>0000-1111=>1111=>15
"""
'''
print(10^5)
a=int(input())
salary=(float(input()))
if a>5:
    salary=salary+((5/100)*salary)
print(salary)    '''
'''
q=int(input())
if q*100>1000:
    print("cost is ",((q*100)-(0.1*q*100)))
else:
    print("cost is ",q*100)
'''
'''
nt=int(input())
res=""
if nt<25:
    res="F"
elif nt>=25 and nt<45:
    res="E"
elif nt>=45 and nt<50:
    res="D"
elif nt>=50 and nt<60:
    res="C"
elif nt>=60 and nt<80:
    res="B"
elif nt>=80:
    res="A"
print(res)
'''

'''
while
 syntax:
     while(condition):
         //stat
         if the condition is 1 then it is infinite loop
         
for 


for else
while-else


#1.while
n=1234324424
su=0
while (n!=0):
    n1=n%10
    su=(su*10)+n1
    n=n//10
print(su)    
'''
#2.for










