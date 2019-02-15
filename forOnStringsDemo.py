#program to apply for loop on strings
#string is collections of characters.

name=input("enter a name") #read name from the user
counter=0
ov=""
for ch in name: #pick each character
     print(ch)
     if(ch=='a' or ch=='e' or ch=='i' or ch=='u' or ch=='o'):
          counter=counter+1
          ov=ov+" "+ch
print("ovel characters are: ",ov)
print("Total ovels are: " , counter)

