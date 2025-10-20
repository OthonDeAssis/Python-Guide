#Typecasting Examples in Python
#Author: Othon DeAssis
#Followed to: BroCode Python's YouTube Guide
#Purpose: Converting one data type to another data type

name = "Othon"
age = 21
height = 5.9
is_student = True

#Outputs the type of variable
print(type(name)) 
print(type(age)) 
print(type(height)) 
print(type(is_student)) 

age = str(age)
print(age)

age = float(age)
print(age)

height = int(height)
print(height)

name = bool(name)
print(name) #If the string is not empty, it will return True, and if it is empty, it will return False.

