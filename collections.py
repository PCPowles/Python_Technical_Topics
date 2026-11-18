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
# ==============================

# Define a list and a string
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
print(my_list)
print(my_string)
print("=============================")

# Slicing: my_list[start:end], 'start' inclusive, end 'exclusive'
slice_list = my_list[2:4]      # [3, 4]
slice_string = my_string[1:3]  # 'el'
print(slice_list)
print(slice_string)
print("=============================")



# Concatenation: my_list + another list
concatenate_list = my_list + [6, 7, 8]
concatenate_string = my_string + ", world!"
print(concatenate_list)
print(concatenate_string)
print("=============================")



# Repetition: my_list * n #
repeat_list = my_list * 2
repeat_string = my_string * 2 
print(repeat_list)
print(repeat_string)
print("=============================")


# Finding the first occurance of an element in a list or string 
# Note that if element is not found, 'index' throws an exception
# So we should initially check the existence of the operator 'in',
#  Then use the index method if it exists usingthe 'if-else' construction.
# If the element is not found, the indeces are assigned to '-1' 
#
#
found_1_in_list = 1 in my_list # Returns: True
print(found_1_in_list)
print("=============================")

found_8_in_list = 8 in my_list # Returns: False
print(found_8_in_list)
print("=============================")

found_l_in_string = 'l' in my_string.lower() # Returns: True
print(found_l_in_string)
print("=============================")

index_1_in_list = my_list.index(1) if found_1_in_list else -1 # Returns: 0
print(index_1_in_list)
print("=============================")

index_8_in_list = my_list.index(8) if found_8_in_list else -1 # Returns: -1
print(index_8_in_list)
print("=============================")


# PCP Check
# Under the hood, Python's bool data type is actually a subclass of int, 
# which means True and False behave directly like integers in comparisons and math
# found_8_in_list_t_f = True if found_8_in_list else False
# print(found_8_in_list_t_f)

index_in_string = my_string.lower().index('l') if found_l_in_string else -1 # Returns: 2
print(index_in_string)
print("============================")

# Sorting items in a list
sorted_list = sorted(my_list, reverse=True) # Returns [5,4,3,2,1]
print(sorted_list)
print("===========================")