""" 

Chapter-1  Variables and types
Author:    AdarshSr
Python Ver: 3.6


"""

# Variables in python are actually an instance of their respective classes.
# Because in python everything is Object Oriented.

# So why does it have a name of variable??

# Because a variable means, an object whose values can keep changing, 
# throughtout the course of the program, and hence it is called Variable. 
# It is perfectly fine if you want to call it an object, just remember 
# it's name and type, which leads us to the second reason why we are 
# calling it a variable, because it makes simple to remember the value 
# and the type of that value that had been stored in it. 

# So let's create some to see what it exaclty looks like.

# How to create a variable or object??
# var = value
# Simple, like that!
# It is completely possible to store value from one variable in to other.
# var1 = var
# How to print the value of my variable??
# You will print the value of your variable using the in-built print() function.
# Example - print(var1)
# Example - print(var)
# How to check what class does my variables belongs to??
# To check the class your variables belongs to, you will have to use the python's 
# in-built type() function.
# Example = type(var1)
# Example = type(var)

# It is important to know that python is a loosely typed language. 
# So it will never restrict you in writing your code, except the indentation part. 
# But Variable with capital V and variable with small V are two different 
# variables for python. 

# Following is a String variable or object, belonging to a String Class.
myname = 'Adarsh'
message = "This isn't the right way to talk with elders"
empty = ''
# Strings can be denoted either by single quotes ' ', or double quotes " ".
# Single quotes are good for storing single values or something that doesn't 
# require a extra bit of single quotes in it. Strings can also be empty at 
# initial stage.
# Now to check what class does it belongs to
typeof_my_name = type(myname)
typeof_messages = type(message)
typeof_empty = type(empty)
# print(typeof_my_name)
# print(typeof_messages)
# print(typeof_empty)
# This code will return a Class associated with this object. For this example 
# it will return <Class 'string'>

# Following is an Integer Variable or object, belonging to an Integer Class.
age = 20
add = 20 + 40
sub = 50 - 30
mul = 9 * 2
power = 5 ** 2
# For integer types you don't require to wrap the values around the quotes.
type(age)
type(add)
type(sub)
type(mul)
type(power)
# This code will return a Class associated with this object. For this example 
# it will return <Class 'Integer'>

# Following is a Float Variable or object, belonging to a Float Class.
speed = 27.8
div = 5 / 2
mod = 2 % 5
# For float types you don't require to wrap the values around the quotes. 
# Float takes in values with decimal point. 
type(speed)
type(div)
type(mod)
# This code will return a Class associated with this object. For this example 
# it will return <Class 'float'>

# Following is a Boolean Variable or object, belonging to a Boolean Class.
is_it_morning = True
is_it_sexy = False
# For Boolean types you don't require to wrap the values around the quotes. 
# Boolean types are denoted by either True or False. It helps to make variables, 
# like an on/off switch.
type(is_it_morning)
type(is_it_sexy)
# This code will return a Class associated with this object. For this example 
# it will return <Class 'bool'>

# All the types will be returned in Quotes. Please open the python Interactive shell 
# and type them after the >>> to move along with the course.

"""
End Of Chapter One

"""