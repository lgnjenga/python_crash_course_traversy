"""
    List: 
    - a collection that is ordered and changeable. Allows duplicate memebers
    - like arrays in javascript
"""

# Create List
numbers = [1, 2, 3, 4, 5]
cars = ['Toyota', 'Audi', 'BMW', 'Ford', 'Mobius']

# Create list using a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(f"{numbers}\n{numbers2}")

# Get a single value
print(cars[1])

# Get length of List
print(len(cars))

# Append to list with append
cars.append('BYD')
cars.append('Tesla')
print(cars)

# Remove from List with remove
cars.remove('BMW')
print(cars)

# Insert into position with insert
cars.insert(3, 'Porshe')
print(cars)

# Change value at position
cars[5] = 'Isuzu'
print(cars)

# Remove from position with pop
cars.pop(4)
print(cars)

# Reverse order with reverse
cars.reverse()
print(cars)

# Sort alphabetically using sort
cars.sort()
print(cars)

# Reverse Sort Alphabetically
cars.sort(reverse=True)
print(cars)