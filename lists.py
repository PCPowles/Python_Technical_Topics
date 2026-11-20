# Lists
# https://practical.learnpython.dev/02_data_types/30_lists/

'''
Notice that we can also optionally add a trailing comma after the last item. 
A trailing comma isn’t required to create a valid list, 
but it does help minimize version control differences when working on a Python codebase with a team.

>>> # Lists
>>> []
[]
>>> type(list())
<class 'list'>
>>> type([])
<class 'list'>
>>> name = ["Nina", "Max", "Jane"]
>>> print(name)
['Nina', 'Max', 'Jane']
>>> len(nbames)
Traceback (most recent call last):
  File "<python-input-120>", line 1, in <module>
    len(nbames)
        ^^^^^^
NameError: name 'nbames' is not defined. Did you mean: 'name'?
>>> len(name)
3
>>> name[0]
'Nina'
>>> name[1]
'Max'
>>> name[2]
'Jane'
>>> # Update
>>> name[2] = "Floyd"
>>> print(name)
['Nina', 'Max', 'Floyd']
>>> len(name)
3
>>> name[3]
Traceback (most recent call last):
  File "<python-input-129>", line 1, in <module>
    name[3]
    ~~~~^^^
IndexError: list index out of range
>>> names = [
... "Nina",
... "Max",
... "Jane",
... ]
>>> print(names)
['Nina', 'Max', 'Jane']
>>> # Sorting
>>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
>>> sorted(lottery_numbers)
[1, 2, 4, 11, 45, 32423]
>>> lottery_numbers
[1, 4, 32423, 2, 45, 11]
>>> sorted(lottery_numbers, reverse=True)
[32423, 45, 11, 4, 2, 1]
>>> lottery_numbers
[1, 4, 32423, 2, 45, 11]
>>> # Sorting the list in-place
>>> 
>>> 

'''