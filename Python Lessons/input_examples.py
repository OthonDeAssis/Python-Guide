#Input Examples in Python
#Author: Othon DeAssis
#Followed to: BroCode Python's YouTube Guide
#Purpose: To demonstrate how to take user input in Python

name = input("What is your name?: ") #Input function always returns a string
age = input("How old are you?: ") #This would output a string

print(f"Hello {name}!")
print(f"You are {age} years old.")
age = int(age)  #Typecasting the input string to an integer
age = age + 1 #To show you must typecast to do mathematical operations.  You can't add an integer to a string.
print(f"You will be {age} years old next year!")
#Remember, you only need to put an 'f' before the string if you are using variables inside the string.

#Exercise 1: Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area}.")

#Exercise 2: Shopping Cart Program
item = input("What item do you want to buy?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int(input(f"How many {item}s do you want to buy?: "))
total_cost = price * quantity
print(f"The total cost for {quantity} {item}(s) is: ${total_cost}")