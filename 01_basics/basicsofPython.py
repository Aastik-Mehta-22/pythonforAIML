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