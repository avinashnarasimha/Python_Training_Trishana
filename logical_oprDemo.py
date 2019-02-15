#program to understand the if...elif ...else statements, along with the logical operators
import sys #importing a module or library
 
x=int(input("enter x number"))
y=int(input("enter y number"))
z=int(input("enter z number"))

"""if x==y or x==z:
     print("values are same")
     sys.exit(0) #exit from the code.
if(z==x or z==y):
     print("values are same")
     sys.exit(0) #exit from the code.
     """

if x >=y and x>=z:
     print("x= %d is big" %(x))
elif y>=x and y>=z:
           print("y= %d is big" %(y))
else:
          print("z = %d is big " %(z))
