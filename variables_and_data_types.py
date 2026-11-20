# Variables and Data Types
# https://practical.learnpython.dev/02_data_types/05_variables_and_types/

'''
PS C:\dev\Python_Technical_Topics> & c:/dev/Python_Technical_Topics/.venv/Scripts/Activate.ps1
(.venv) PS C:\dev\Python_Technical_Topics> & c:/dev/Python_Technical_Topics/.venv/Scripts/python.exe
Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> x = 1
>>> y=2
>>> x+y
3
>>> 
(.venv) PS C:\dev\Python_Technical_Topics> 
(.venv) PS C:\dev\Python_Technical_Topics> 
(.venv) PS C:\dev\Python_Technical_Topics> & c:/dev/Python_Technical_Topics/.venv/Scripts/python.exe
Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> import antigravity
>>> 
(.venv) PS C:\dev\Python_Technical_Topics> python -m pip install requests
Collecting requests
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Using cached charset_normalizer-3.5.2-cp315-cp315-win_amd64.whl.metadata (47 kB)
Collecting idna<4,>=2.5 (from requests)
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting certifi>=2023.5.7 (from requests)
  Using cached certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached charset_normalizer-3.5.2-cp315-cp315-win_amd64.whl (210 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
Successfully installed certifi-2026.10.23 charset_normalizer-3.5.2 idna-3.20 requests-2.34.2 urllib3-2.8.0

[notice] A new release of pip is available: 26.2.1 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\dev\Python_Technical_Topics> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in .\.venv\Lib\site-packages (26.2.1)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 14.0 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 26.2.1
    Uninstalling pip-26.2.1:
      Successfully uninstalled pip-26.2.1
Successfully installed pip-26.3
(.venv) PS C:\dev\Python_Technical_Topics> 
(.venv) PS C:\dev\Python_Technical_Topics> & c:/dev/Python_Technical_Topics/.venv/Scripts/python.exe
Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> x=42
>>> x="hello"
>>> print(x)
hello
>>> num = 42
>>> type(num)
<class 'int'>
>>> num
42
>>> x = 1
>>> x
1
>>> x = None
>>> x
>>> name = "Nina"
>>> type(name)
<class 'str'>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help()
Welcome to Python 3.15's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.15/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

You can use the following keyboard shortcuts at the main interpreter prompt.
F1: enter interactive help, F2: enter history browsing mode, F3: enter paste
mode (press again to exit).

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 

'''