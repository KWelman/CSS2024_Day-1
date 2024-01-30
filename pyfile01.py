# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:42:10 2024

@author: welman
"""

print("My First Python File")
#This is my first comment

#Valid Names
x = 50
age = 50
_age = 50
my_age = 50
mYagE = 50
my_age_2 = 50

"""
It is recommended that when naming variables you follow the following rules:
A variable can have a short name like x or y or more descriptive ones like age, myage, countrylist.
A variable must start with a letter or underscore
A variable cannot start with a number
A variable can only contain alpha-numeric characters and underscores
A variable name is case-sensitive: age, Age, and AGE are all different variable names
"""

# Invalid names

2age = 50 #can't start with a numerical value
my age = 50 #add an underscore for spaces
my-age = 50 #add an underscore for spaces

# An integer and a string are two different types of data that can be used in programming. An integer is a whole number, such as 42, while a string is a sequence of characters, such as “Hello”. They have different properties and operations, and cannot be directly combined without conversion.

# This works because both are integers
x = 10
y = 20
z = x + y
print(z) # Prints 30

# This works because both are strings
a = "Hello"
b = "World"
c = a + b
print(c) # Prints HelloWorld

# This does not work because one is an integer and one is a string
d = "42"
e = 10
f = d + e
print(f) # Raises a TypeError

# This works because we convert the integer to a string first
g = "42"
h = 10
i = g + str(h)
print(i) # Prints 4210

# This works because we convert the string to an integer first
j = "42"
k = 10
l = int(j) + k
print(l) # Prints 52

# a float or a variable number that has decimals.

