# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

a = []

for human in humans:
    if human.name.startswith('D'):
        a.append(human.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

b = []

for human in humans:
    if human.name.endswith('e'):
        b.append(human.name)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

letters = ['C', 'D', 'E', 'F', 'G']
names = []

for human in humans:
    names.append(human.name)

c = [name for name in names if (name[0] in letters)]

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.

d = []

for human in humans:
    age = human.age + 10
    d.append(age)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.

e = []

for human in humans:
    hyphen = f"{human.name}-{human.age}"
    e.append(hyphen)

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

f = []

for human in humans:
    if human.age in range(27 , 33):
        name = human.name
        age = human.age
        syntax = name, age
        f.append(syntax)

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

g = []

for human in humans:
    name = human.name.upper()
    age = human.age + 5
    g.append(Human(name, age))

print(g)

# Write a list comprehension that contains the square root of all the ages.

import math
h = []
ages = []

for human in humans:
    ages.append(human.age)

for age in ages:
    sqrt = math.sqrt(age)
    h.append(sqrt)

print(h)
