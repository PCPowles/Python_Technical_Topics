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

>>> 
>>> lottery_numbers.sort()
>>> print(lottery_numbers)
[1, 2, 4, 11, 45, 32423]
>>> lottery_numbers.sort(reverse=True)
>>> print(lottery_numbers)
[32423, 45, 11, 4, 2, 1]
>>> words = ["Umbrella","Fox","Apple"]
>>> words.sort()
>>> words
['Apple', 'Fox', 'Umbrella']
>>> # Reverse the list in-place
>>> lottery_numbers.reverse()
>>> lottery_numbers
[1, 2, 4, 11, 45, 32423]
>>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
>>> lottern_numbers
Traceback (most recent call last):
  File "<python-input-151>", line 1, in <module>
    lottern_numbers
NameError: name 'lottern_numbers' is not defined. Did you mean: 'lottery_numbers'?
>>> lottery_numbers
[1, 4, 32423, 2, 45, 11]
>>> lottery_numbers.reverse()
>>> lottery_numbers
[11, 45, 2, 32423, 4, 1]
>>> # Finding Methods
>>> 

>>> 
>>> list.dir()
Traceback (most recent call last):
  File "<python-input-157>", line 1, in <module>
    list.dir()
    ^^^^^^^^
AttributeError: type object 'list' has no attribute 'dir'
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list)
Help on class list in module builtins:                                                                                                        

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.                                                                                                                   
 |                                                                                                                                            
 |  __getitem__(self, index, /)                                                                                                               
 |      Return self[index].                                                                                                                   
 |                                                                                                                                            
 |  __gt__(self, value, /)                                                                                                                    
 |      Return self>value.                                                                                                                    
 |                                                                                                                                            
 |  __iadd__(self, value, /)                                                                                                                  
 |      Implement self+=value.                                                                                                                
 |                                                                                                                                            
 |  __imul__(self, value, /)                                                                                                                  
 |      Implement self*=value.                                                                                                                
 |                                                                                                                                            
 |  __init__(self, /, *args, **kwargs)                                                                                                        
 |      Initialize self.  See help(type(self)) for accurate signature.                                                                        
 |                                                                                                                                            
 |  __iter__(self, /)                                                                                                                         
 |      Implement iter(self).                                                                                                                 
 |                                                                                                                                            
 |  __le__(self, value, /)                                                                                                                    
 |      Return self<=value.                                                                                                                   
 |                                                                                                                                            
 |  __len__(self, /)                                                                                                                          
 |      Return len(self).                                                                                                                     
 |                                                                                                                                            
 |  __lt__(self, value, /)                                                                                                                    
 |      Return self<value.                                                                                                                    
 |                                                                                                                                            
 |  __mul__(self, value, /)                                                                                                                   
 |      Return self*value.                                                                                                                    
 |                                                                                                                                            
 |  __ne__(self, value, /)                                                                                                                    
 |      Return self!=value.                                                                                                                   
 |                                                                                                                                            
 |  __repr__(self, /)                                                                                                                         
 |      Return repr(self).                                                                                                                    
 |                                                                                                                                            
 |  __reversed__(self, /)                                                                                                                     
 |      Return a reverse iterator over the list.                                                                                              
 |                                                                                                                                            
 |  __rmul__(self, value, /)                                                                                                                  
 |      Return value*self.                                                                                                                    
 |                                                                                                                                            
 |  __setitem__(self, key, value, /)                                                                                                          
 |      Set self[key] to value.                                                                                                               
 |                                                                                                                                            
 |  __sizeof__(self, /)                                                                                                                       
 |      Return the size of the list in memory, in bytes.                                                                                      
 |                                                                                                                                            
 |  append(self, object, /)                                                                                                                   
 |      Append object to the end of the list.                                                                                                 
 |                                                                                                                                            
 |  clear(self, /)                                                                                                                            
 |      Remove all items from list.                                                                                                           
 |                                                                                                                                            
 |  copy(self, /)                                                                                                                             
 |      Return a shallow copy of the list.                                                                                                    
 |                                                                                                                                            
 |  count(self, value, /)                                                                                                                     
 |      Return number of occurrences of value.                                                                                                
 |                                                                                                                                            
 |  extend(self, iterable, /)                                                                                                                 
 |      Extend list by appending elements from the iterable.                                                                                  
 |                                                                                                                                            
 |  index(self, value, start=0, stop=9223372036854775807, /)                                                                                  
 |      Return first index of value.                                                                                                          
 |                                                                                                                                            
 |      Raises ValueError if the value is not present.                                                                                        
 |                                                                                                                                            
 |  insert(self, index, object, /)                                                                                                            
 |      Insert object before index.                                                                                                           
 |                                                                                                                                            
 |  pop(self, index=-1, /)                                                                                                                    
 |      Remove and return item at index (default last).                                                                                       
 |                                                                                                                                            
 |      Raises IndexError if list is empty or index is out of range.                                                                          
 |                                                                                                                                            
 |  remove(self, value, /)                                                                                                                    
 |      Remove first occurrence of value.                                                                                                     
 |                                                                                                                                            
 |      Raises ValueError if the value is not present.                                                                                        
 |                                                                                                                                            
 |  reverse(self, /)                                                                                                                          
 |      Reverse *IN PLACE*.                                                                                                                   
 |                                                                                                                                            
 |  sort(self, /, *, key=None, reverse=False)                                                                                                 
 |      Sort the list in ascending order and return None.                                                                                     
 |                                                                                                                                            
 |      The sort is in-place (i.e. the list itself is modified) and stable                                                                    
 |      (i.e. the order of two equal elements is maintained).                                                                                 
 |                                                                                                                                            
 |      If a key function is given, apply it once to each list item and sort                                                                  
 |      them, ascending or descending, according to their function values.                                                                    
 |                                                                                                                                            
 |      The reverse flag can be set to sort in descending order.                                                                              
 |                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                    
 |  Class methods defined here:                                                                                                               
 |                                                                                                                                            
 |  __class_getitem__(object, /)                                                                                                              
 |      lists are generic over the type of their contents                                                                                     
 |                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                    
 |  Static methods defined here:                                                                                                              
 |                                                                                                                                            
 |  __new__(*args, **kwargs)                                                                                                                  
 |      Create and return a new object.  See help(type) for accurate signature.                                                               
 |                                                                                                                                            
 |  ----------------------------------------------------------------------                                                                    
 |  Data and other attributes defined here:                                                                                                   
 |                                                                                                                                            
 |  __hash__ = None                                                                                                                           

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help(list.append)
Help on method descriptor append:                                                                                                             

append(self, object, /) unbound builtins.list method
    Append object to the end of the list.

>>> len(names)
3
>>> names
['Nina', 'Max', 'Jane']
>>> name = "Nina"
>>> len(name)
4
>>> names = ["Nina","Max"]
>>> names
['Nina', 'Max']
>>> names.append("John")
>>> list
<class 'list'>
>>> names
['Nina', 'Max', 'John']
>>> type(names)
<class 'list'>
>>> names.insert(0, "Rose")
>>> names
['Rose', 'Nina', 'Max', 'John']
>>> help names.insert()
  File "<python-input-198>", line 1
    help names.insert()
         ^^^^^
SyntaxError: invalid syntax
>>> help (names.insert)
Help on built-in function insert:                                                                                                             

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> names = ["Nina","Max"]
>>> colors = ["Red","Blue"]
>>> names
['Nina', 'Max']
>>> colors
['Red', 'Blue']
>>> names.extend(colors)
>>> names
['Nina', 'Max', 'Red', 'Blue']
>>> "Nina" in names
True
>>> "Rose" in names
False
>>> names.index("Nina")
0
>>> names.index("Rose")
Traceback (most recent call last):
  File "<python-input-209>", line 1, in <module>
    names.index("Rose")
    ~~~~~~~~~~~^^^^^^^^
ValueError: list.index(x): x not in list
>>> names.index("Max")
1
>>> names
['Nina', 'Max', 'Red', 'Blue']
>>> names.count("Nina")
1
>>> names = ["Nina", "Max", "Phillip", "Nina"]
>>> names.count("Nina")
2
>>> names.count("Rose")
0
>>> ## Updating Items ##
>>> 
>>> 
>>> 
>>> names = ["Nina","Max"]
>>> names[0] = "Rose"
>>> names
['Rose', 'Max']
>>> names = ["Nina","Max"]
>>> pos = names.index("Max")
>>> pos
1
>>> names[pos] = "Rose"
>>> names
['Nina', 'Rose']
>>> 
>>> 
>>> 
>>> names=s ["Nina","Max"]
Traceback (most recent call last):
  File "<python-input-231>", line 1, in <module>
    names=s ["Nina","Max"]
          ^
NameError: name 's' is not defined
>>> names= ["Nina","Max"]
>>> len(names)
2
>>> names[2] = "Rose"
Traceback (most recent call last):
  File "<python-input-234>", line 1, in <module>
    names[2] = "Rose"
    ~~~~~^^^
IndexError: list assignment index out of range
>>> 
>>> 
>>> ## Removing Items ##
>>> names = ["Nina","Max","Rose"]
>>> names.remove("Nina")
>>> names
['Max', 'Rose']
>>> 
>>> 
>>> names = ["Nina","Max","Rose"]
>>> names = ["Nina","Max","Nina"]
>>> names.remove("Nina")
>>> names
['Max', 'Nina']
>>> 

Adding, Removing, Changing, and Finding Items in lists cheat sheet
------------------------------------------------------------------------------------------------------------------------------------
action	                                method	                    returns	                possible errors
------------------------------------------------------------------------------------------------------------------------------------
check length	                        len(my_list)	                    int	
add: to the end	                        my_list.append(item)	            -	
insert: at position	                    my_list.insert(pos, item)	        -	
update: at position	                    my_list[pos] = item	                - -	           IndexError if pos is >= len(my_list)
extend: add items from another list	    my_list.extend(other_list)	        -	
is item in list?	                    item in my_list	            True or False	
index of item	                        my_list.index(item)	                int	            ValueError if item is not in my_list
count of item	                        my_list.count(item)	                int	
remove an item	                        my_list.remove(item)	            -	            ValueError if item not in my_list
remove the last item, 
or an item at an index	                my_list.pop() or my_list.pop(pos)	item	        IndexError if pos >= len(my_list)



'''