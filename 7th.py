#print("Enter the no of students are interested in jooining the group:")
n=int(input("Enter the no of students are interested in jooining the group:"))
num=[]
print("Enter the names of the participants:\n")
for i in range(n):
    element=input("Enter the member:") 
    num.append(element)
print("the members are successfuly added!/\!:)}") 
print("Haha you want to search the elements in the list?\nthemn go a head:")
sty=input("What name you want to find:")
ic=int(0)
for ss in num:
   ic=ic+1 
   if ss==sty:
      print("Found the name of the person at index",i)
  
       
           