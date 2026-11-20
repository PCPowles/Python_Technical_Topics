# Strings
# https://practical.learnpython.dev/02_data_types/20_strings/

'''
>>> # Strings
>>> greeting = 'Hello, it\'s Nina'
>>> greeting
"Hello, it's Nina"
>>> greeting = "Hello, it's Nina"
>>> greeting
"Hello, it's Nina"
>>> long_greeting = """Greetings and salutations, dear Nina.
...                 I'm superfluous with my words,
...                 and require more space to say Hello!"
...                 """
>>> long_greeting
'Greetings and salutations, dear Nina.\n                I\'m superfluous with my words,\n                and require more space to say Hello!"\n                '
>>> print("Hello")
Hello
>>> name = "Nina"
>>> print(name)
Nina
>>> print("October is month", 10)
October is month 10
>>> # Concatenation
>>> salutation = "Hello "
>>> name = "Nina"
>>> greeting = salutation + name
>>> print(greeting)
Hello Nina
>>> # f-strings
>>> name = "Nina"
>>> greeting = f"Hello, {name}"
>>> print(greeting)
Hello, Nina
>>> # Trimming a string
>>> 
>>> my_string = "   Hello world!   "
>>> print(my_string)
   Hello world!   
>>> print(f">{my_string.strip()}<")
>Hello world!<
>>> my_string = "Hello World!,,,"
>>> print(my_string)
Hello World!,,,
>>> print(my_string.strip(","))
Hello World!
>>> 
>>> # Replacing Characters
>>> 
>>> my_string = "Hello World!"
>>> print(my_string)
Hello World!
>>> my_string.replace("world","Nina")
'Hello World!'
>>> print(my_string)
Hello World!
>>> my_string.replace("World","Nina")
'Hello Nina!'
>>> print(my_string)
Hello World!
>>> # Working with strings
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.title)
Help on method descriptor title:                                                                                                              

title(self, /) unbound builtins.str method
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all
    remaining cased characters have lower case.

>>> # strformat() and % formatting
>>> 
>>> name = "Nina"
>>> print("Hello, my name is {name}".format(name=name))
Hello, my name is Nina
>>> name = "Nina"
>>> print("Hello, my name is %s" % name)
Hello, my name is Nina
>>> # For formatting strings in modern Python, reach for f-strings instead.
>>> 

'''