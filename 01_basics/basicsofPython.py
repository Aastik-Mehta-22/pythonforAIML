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
