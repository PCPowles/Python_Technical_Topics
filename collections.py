# Collections

# Defining a list and a string
my_list = [1,2,3,4]
print(my_list)
print("=============================")
my_string = 'hello'
print("=============================")


# Now let's try to change the first element of both these collections
my_list[0] = 100
print(my_list)
print("=============================")

# This will produce an error
##  my_string[0] = 'H'
## print(my_string)
print("=============================")

'''
word = "hello"
word = "j" + word[1:]
print(word)  # Output: jello
#
word = "hello"
word = word.replace("h", "j", 1)
print(word)  # Output: jello
'''

# Creating a list
fruits = ['apple','banana','cherry']
print(fruits)
print("=============================")



# Add a new element at the end
fruits.append('date')
print(fruits)
print("=============================")



# Inserting an element at a certain location
fruits.insert(1, 'bilberry')
print(fruits)
print("=============================")



# Removing a particular element
fruits.remove('banana')
print(fruits)
print("=============================")



# Accessing elements using indexing
first_fruit = fruits[0]
last_fruit = fruits[-1]
print(first_fruit)
print(last_fruit)
print("=============================")



# Understanding Strings
# https://codesignal.com/learn/course/90/unit/2


# Creating a string
greeting_string = "Hello, world!"
print(greeting_string)
print("=============================")

# Accessing characters using indexing
first_char = greeting_string[0] # 'H'
last_char = greeting_string[-1] # '!'
print(first_char)
print(last_char)
print("=============================")

lowercase_greeting = greeting_string.lower() # "hello world!"
print(lowercase_greeting)
print("=============================")

'''
Though strings are immutable, 
we can use string methods such as .lower(), .upper(), .strip(), etc., 
to effectively work with them. These methods essentially create a new string for us.
'''


# Indexing and Common Operations

