# 🖨️ Python print()
# The print() function is used to display output on the screen in Python.
# Basic Syntax

print("Hello")
print("Hello, World!")

# Printing Text


print("Welcome to Python")

print("my name is maneesh")

# Printing Numbers

print(35)
print(10 + 30)
print(10 * 5)

# Printing Variables

name = "maneesh"
age = 40
work = "devops"

print(name)
print(age)
print(work)

# Printing Multiple Values

name = "maneesh"
age = 40
work= "devops engineer"

print(name, age,work)

# sep Parameter

# The sep parameter defines what is placed between multiple values.

print("maneesh", "Chiku", "krishu", sep="-")

print("20", "05", "2016", sep="/")

# end Parameter
# By default, print() adds a newline after printing.

print("Hello")
print("World")

print("Hello", end="-")
print("World")

print("Hello", end="**")
print("World")


# Escape Characters

# New Line - \n
print("Hello Dosto\nMera Naam\nmaneesh Hai")

# # # Tab - \t
# print("Hello Dosto\tMera Naam\tmaneesh Hai\tEngineer")
print("Name\tAge")
print("Amit\t30")


# Escape Characters

# New Line - \n
print("Hello Dosto\nMera Naam\nAmit Hai")

# # Tab - \t
print("Hello Dosto\tMera Naam\tAmit Hai")
print("Name\tAge")
print("Amit\t30")

# Quote

print("Hi Friends \"To Kaise Hn Aap log?\" kaisa raha aaj aapa din?\"")


# Printing with Variables

# Using comma

name = "maneesh"
age = 40

print("Name:", name)
print("Age:", age)
print("Hi Dosto, Mera Naam", name, "Hai aur Mai", age, "Saal Ka Hoon.")

# Using f-string

name = "maneesh"
age = 40

print(f"My name is {name} and I am {age} years old.")

# Printing Expressions

a = 10
b = 20

print(a + b)
print(a * b)
print(a > b)

# Printing Different Data Types

name = "maneesh kumar"
age = 40
salary = 60000
is_active = True

print(name)
print(age)
print(salary)
print(is_active)

# Printing Lists

fruit = ["banana", "apple", "guava","mango"]
print(fruit)



# Printing Dictionaries

user = {
    "name": "Maneesh",
    "role": "DevOps Engineer"
}

print(user)

# Important print() Parameters

# *objects  -> Values to print
# sep       -> Separator between values
# end       -> Character/string printed at the end
# file      -> Where the output is written
# flush     -> Whether to forcibly flush the output

print("Python", "Docker", "Kubernetes", sep=" | ", end="\n")

# Real-World Example

name = "maneesh"
role = "Cloud & DevOps Engineer"
experience = 7

print("Name:", name)
print("Role:", role)
print("Experience:", experience, "years")

