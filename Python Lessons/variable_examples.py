#Input Examples in Python
#Author: Othon DeAssis
#Followed to: BroCode Python's YouTube Guide
#Purpose: This program is meant to practice Variables in Python (String, Integer, Float, Boolean)


# - Strings: Storing text data
first_name = "Othon"
last_name = "DeAssis"
gaming_username = "Obnoxious"
print(first_name)
print(last_name)
print(gaming_username)
print(f"Hello, {first_name} {last_name}, also known as online {gaming_username}!")

#Integers: Whole numbers
age = 21
programming_years = 5
favorite_number = 73
print(f"I am {age} years old, I have been programming for {programming_years} and my favorite number is {favorite_number}.")

#Floats: Decimal numbers
price = 10.99
print(f"The price of the item is ${price}.")
price = 20.5
price = f"{price:.2f}"  # Adds trailing zeroes, making the output "20.50" even though the input was 20.5.
price_with_5_decimals = f"{20.5:.5f}"
print(f"{price_with_5_decimals}") #You can add more zeros (.3f -> "20.500") or remove decimals (.0f -> "20")
print(f"The price of the item is ${price}.")

gpa = 3.5
print(f"My GPA is {gpa}.")
distance = 12.75
print(f"The distance to the destination is {distance} miles.")

precise_distance = 12.754321 #To add more precision, you can use more decimal places
print(f"The precise distance to the destination is {distance} miles.")


#Booleans: True or False values
is_student = True
has_graduated = False
print(f"Am I a student? {is_student}")
print(f"Have I graduated? {has_graduated}")