#arithmetic operators (+ - * / %)

x=float(input("enter marks1"))
y=float(input("enter marks2"))
z=x+y
z1=x-y
z2=x/y
z3=x*y
z4=1-(x/y)

#%d %s %f required if you are printing a message along with the number
# else simple print will do

print ("sum of %d and %d is: %d"%(x,y,z))
#alternatively print ("sum of %d and %d is: %d"%(x,y,x+y))
# you can convert to any format in the print statement itself %d %s %f
print ("difference of %d and %d is: %d"%(x,y,z1))
print ("Multiplication of %d and %d is: %d"%(x,y,z3))
print ("Division of %d and %d is: %d"%(x,y,z2))
print ("Percentage of %d and %d is: %d"%(x,y,z4))


'''
OUTPUT----------
enter marks1100
enter marks250
sum of 100 and 50 is: 150
difference of 100 and 50 is: 50
Multiplication of 100 and 50 is: 5000
Division of 100 and 50 is: 2
Percentage of 100 and 50 is: -1'''
