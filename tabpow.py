print("completetion of two programs:\n1.print tablesof respective nuumber\n2.power using power function\nFirst print tables")
nn=int(input("Enter the number  of the table:"))
mm=int(input("Enter the number of rows:"))
i=1
for i in range(1,mm+1):
    print(nn," * ",i," = ",nn*i)
print(50*'*')
print("second- program") 
num=int(input("Enter the number: "))
power=int(input("Enter the power of the number: ")) 
print("The value of the number is ",pow(num,power))
  