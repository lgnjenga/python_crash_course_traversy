"""
    Strings and String Formatting and String Methods
    - Strings in Python are either surrounded by single or double quotation marks
"""

name = 'Tosh'
age = 33

'''
    1. Concatenate
'''
# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old')

'''
    a) String Formatting
    - Insert Variables into Strings
'''

'''
    2. Arguments by Position
'''
#print('Hello, my name is {name} and I am {age} years old'.format(name=name, age=age))

'''
    3. F-Strings (Only works on Python3.6 and above)
'''
print(f'Hello, my name is {name} and I am {age} years old')

'''
    b) String Methods
'''
s = 'helloWorld'

# Capitalize
print(s.capitalize())

# Make All Uppercase
print(s.upper())

# Make all Lowercase
print(s.lower())

# Swap Case
print(s.swapcase())

# Get Length
print(len(s))

# Count: Number of occurences of substrings inside the string
sub = 'o'
print(s.count(sub))

# Starts with
print(s.startswith('h'))

# End with
print(s.endswith('h'))

# Split string into a list/array of individual words
print(s.split())

# Find the position of a character
print(s.find('o'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())






