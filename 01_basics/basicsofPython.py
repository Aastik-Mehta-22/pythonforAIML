# in python we dont declare a type - the variable just becomes whatever you assign to it
age = 25
price = 99.9
name = "Alex"
is_active = True

# we can even reassign a variable to a completely different type later
# (not a great practice offc but python allows it )
x = 10
x = "I am a legal string"
# why it matters ?
# python figures out the type at runtime, not before.This is called 
# dynamic typing. It's convenient but means python wont catch type mistakes
# until the code actually runs

# Core Data Types
# whole_number = 10 int
# decimal_number = 10.5 float
# text = "hello" string 
# flag = true bool
# nothing = None represents "no value"

print(type(10)) # check any type with type()
print(type(10.5))
print(type("hi"))

# Type Casting (converting between types)
x = "5" 
y = int(x) # 5 (string to int)
z = float(x) # 5.0
s = str(x) # "10" (int to string)

print(y + 10) # 15

# A classic trap
# age = input("Enter your age: ")  Note:- input always returns string
# print(age + 5)  ❌ Error! Can't add int to str
# print(int(age) + 5) ✅ Works

# Operators

#Airthmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333... (always returns a float)
print(10 // 3)  # 3   (floor division — drops the decimal)
print(10 % 3)   # 1   (remainder / modulo)
print(10 ** 2)  # 100 (power)

# Comparison (True/False)
print(5 == 5) #True
print(5 != 3) #True
print(5 > 3) #True

# Logical
print(True and False) # False
print(True or False) # True
print(not True) # False

# Membership
fruits = ["apple", "banana"]
print("apple" in fruits)       # True
print("mango" not in fruits)   # True

#Identity — this one trips people up. == checks value, is checks if it's literally the same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  -> same values
print(a is b)   # False -> different objects in memory

# Strings - Indexing, Slicing, and immutability
# Strings in python are immutable - once created, you can not change a 
# character in place

name = "Python"
# name[0] = "J"   ❌ Error — strings can't be modified this way
name = "J" + name[1:]   # ✅ This creates a brand new string instead

#Indexing starts from 0 negative indices count from the end
name = "Python"
print(name[0])    # 'P' (first character)
print(name[-1])   # 'n' (last character)

# Slicing — name[start:end] gives you a sub-string, 
# where start is included and end is excluded.
print(name[0:3]) # 'Pyt'  -> characters at index 0, 1, 2 (not 3)

# f-strings are the modern way to build strings with variables/expressions embedded:

name, age = "Alex", 25
print(f"{name} is {age} years old, and next year will be {age + 1}")

# Basics of Data Structure


# List — your default choice for a collection of items that might change:
fruits = ["apple", "banana", "cherry"]
# Ordered means the items keep their position; 
# indexable by position (fruits[0]); 
# mutable means we can add/remove/change items after creation.

# Tuple - like a list, but locked (immutable)
point = (10,20)

# why use this instead of a list? 
# Two reasons: (1) it signals to anyone reading your code "this data shouldn't change," 
# and (2) tuples are slightly faster and can be used as dictionary keys 
# (lists cannot, because dict keys must be immutable).


#  Dictionary - the tool for "look something up by a name, instantly"
person = {"name": "Alex", "age": 25}
print(person["name"])   # instant lookup, doesn't matter how big the dict is

# Internally, a dict uses something called hashing —
#  it converts the key into a number and jumps straight to that spot in memory,
#  rather than scanning every item like a list would. 
# That's why dict lookups stay fast even with millions of entries,
#  while searching a huge list gets slower as it grows.


# Set - a collection that automatically removes duplicates and doesn't preserve order
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)   # {1, 2, 3}


# Note :-
# Rule of thumb: 
# need order + duplicates + changeable → list. 
# Need a fixed sequence → tuple.
#  Need to look things up by name → dict. 
# Need uniqueness or fast membership checks → set.