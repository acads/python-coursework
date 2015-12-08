Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> print 'hello'
hello
>>> 
>>> 
>>> # 15 people by 9:35, 10 by 9:26. w00t!
>>> 

>>> # PyPI
>>> 

>>> # pypy
>>> # Jython
>>> # IronPython
>>> 

>>> 
>>> # 70683 packages on https://pypi.python.org/pypi
>>> 
>>> 

>>> 
>>> def f():
	a = 1
	 return
# IndentationError: ('unindent does not match any outer indentation level', ('<tokenize>', 29, 2, '  File "<pyshell#18>", line 3\n'))
a
	
  File "<pyshell#18>", line 3
    return a
    ^
IndentationError: unexpected indent
>>> 
>>> 
>>> 
>>> 
>>> sort([1, 4, 3])

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sort([1, 4, 3])
NameError: name 'sort' is not defined
>>> sorted([1, 4, 3])
[1, 3, 4]
>>> 
>>> 
>>> # REPL
>>> # R-E-P-L
>>> 
>>> # Read
>>> # Evaluate
>>> # Print
>>> # Loop
>>> 
>>> a = 1
>>> a
1
>>> 
>>> # PEP8
>>> 
>>> 
>>> # Break 10:36 to 10:46am
>>> 
>>> 
>>> # Yay we're all here in IDLE
>>> print 'Hello world'
Hello world
>>> 
>>> 

>>> import os
>>> os.getcwd()
'/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace'
>>> 
>>> 
>>> 
>>> 
>>> # python -m idlelib.idle
>>> 
>>> ================================ RESTART ================================
>>> 
====== Source: http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt ======
                      Starting download at Mon Dec  7 10:53:35 2015                       
http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt
200  OK           http://www.bossylobster.com/learning-python/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (updated) 
200  OK           http://www.bossylobster.com/learning-python/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (updated) 
>>> ================================ RESTART ================================
>>> 
====== Source: http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt ======
                      Starting download at Mon Dec  7 10:54:07 2015                       
http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt
304  Not Modified http://www.bossylobster.com/learning-python/shared/raisin_team.csv
304  Not Modified http://www.bossylobster.com/learning-python/shared/PythonAwesome.pdf
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()
'/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace'
>>> 
>>> os.chdir
<built-in function chdir>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> None
>>> None = 10
SyntaxError: cannot assign to None
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> a = 10
>>> a
10
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
>>> del a
>>> a

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> hello

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 'hello'
'hello'
>>> r'hello'
'hello'
>>> 
>>> 'this is a tab\tthat was a tab'
'this is a tab\tthat was a tab'
>>> print 'this is a tab\tthat was a tab'
this is a tab	that was a tab
>>> r'this is a tab\tthat was a tab'
'this is a tab\\tthat was a tab'
>>> 
>>> b'abc'
'abc'
>>> u'abc'
u'abc'
>>> 
>>> 
>>> u'\u201d'
u'\u201d'
>>> print u'\u201d'
”
>>> u'\u201d'.encode('utf-8')
'\xe2\x80\x9d'
>>> print u'\u201d'.encode('utf-8')
”
>>> 
>>> 
>>> type('abc')
<type 'str'>
>>> type(u'abc')
<type 'unicode'>
>>> 
>>> 
>>> 
>>> class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print 'Hi, my name is', self.name

		
>>> 
>>> d = Dog('Fido')
>>> d.bark()
Hi, my name is Fido
>>> d.__class__
<class __main__.Dog at 0x11072f258>
>>> 
>>> dir(d)
['__doc__', '__init__', '__module__', 'bark', 'name']
>>> # What is 0x11072f258?
>>> 
>>> # rm -fr /
>>> dir()
['Dog', '__builtins__', '__doc__', '__name__', '__package__', 'd', 'this']
>>> 
>>> 
>>> 
>>> class Dog:
	def bark(self):
		print 'I do not have a name'

		
>>> d = Dog()
>>> d.bark()
I do not have a name
>>> 
>>> d = Dog('Fido')

Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    d = Dog('Fido')
TypeError: this constructor takes no arguments
>>> 
>>> 
>>> dir()
['Dog', '__builtins__', '__doc__', '__name__', '__package__', 'd', 'this']
>>> 
>>> 
>>> dir()
['Dog', '__builtins__', '__doc__', '__name__', '__package__', 'd', 'this']
>>> dir(d)
['__doc__', '__module__', 'bark']
>>> type(d)
<type 'instance'>
>>> 
>>> class Dog(object):
	def bark(self):
		print 'I do not have a name'

		
>>> d = Dog()
>>> type(d)
<class '__main__.Dog'>
>>> 
>>> d.__class__
<class '__main__.Dog'>
>>> 

>>> 
>>> help('s')
no Python documentation found for 's'

>>> s = [1, 2, 3]
>>> 
>>> type(s)
<type 'list'>
>>> 
>>> help(s)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __delslice__(...)
 |      x.__delslice__(i, j) <==> del x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |  
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __setslice__(...)
 |      x.__setslice__(i, j, y) <==> x[i:j]=y
 |      
 |      Use  of negative indices is not supported.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -- append object to end
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> s
[1, 2, 3]
>>> s.insert
<built-in method insert of list object at 0x11068abd8>
>>> help(s.insert)
Help on built-in function insert:

insert(...)
    L.insert(index, object) -- insert object before index

>>> s
[1, 2, 3]
>>> s.insert(2, 1000)
>>> s
[1, 2, 1000, 3]
>>> 
>>> 
>>> 
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> s
[1, 2, 1000, 3]
>>> 
>>> len(s)
4
>>> s[0]
1
>>> 
>>> 
>>> 
>>> dir(d)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bark']
>>> d
<__main__.Dog object at 0x110717790>
>>> 
>>> d.__dict__
{}
>>> class Dog:
	def __init__(self, name):
		self.name = name

		
>>> d = Dog('Timmy')
>>> d.__dict__
{'name': 'Timmy'}
>>> 
>>> d = Dog()

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    d = Dog()
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> 
>>> 
>>> 
>>> 
>>> class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print 'Hi I am', self.name

		
>>> d = Dog('Fido')
>>> d.bark
<bound method Dog.bark of <__main__.Dog instance at 0x110684e60>>
>>> 
>>> 
>>> d.bark()
Hi I am Fido
>>> Dog.bark
<unbound method Dog.bark>
>>> Dog.bark()

Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    Dog.bark()
TypeError: unbound method bark() must be called with Dog instance as first argument (got nothing instead)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
>>> 
>>> 'abc'
'abc'
>>> r'abc'
'abc'
>>> b'abc'
'abc'
>>> u'abc'
u'abc'
>>> 
>>> 
>>> "abc"
'abc'
>>> 

>>> 'hi i'm fido'
SyntaxError: invalid syntax
>>> "hi i'm fido"
"hi i'm fido"
>>> r'hi i'm fido'
SyntaxError: invalid syntax
>>> 
>>> 
>>> r'ab\tv'
'ab\\tv'
>>> 'hi i\'m fido'
"hi i'm fido"
>>> 
>>> 
>>> '''hi, i'm fido'''
"hi, i'm fido"
>>> """hi, i'm fido"""
"hi, i'm fido"
>>> s

Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = [1, 2, 3]
>>> s
[1, 2, 3]
h
>>> help(s)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __delslice__(...)
 |      x.__delslice__(i, j) <==> del x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |  
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __setslice__(...)
 |      x.__setslice__(i, j, y) <==> x[i:j]=y
 |      
 |      Use  of negative indices is not supported.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -- append object to end
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> print 'restart'
restart
>>> s = 'restart'
>>> help(s)
no Python documentation found for 'restart'

>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> for attribute in dir(s):
	print attribute

	
__add__
__class__
__contains__
__delattr__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__getslice__
__gt__
__hash__
__init__
__le__
__len__
__lt__
__mod__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
_formatter_field_name_split
_formatter_parser
capitalize
center
count
decode
encode
endswith
expandtabs
find
format
index
isalnum
isalpha
isdigit
islower
isspace
istitle
isupper
join
ljust
lower
lstrip
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
>>> s.capitalize()
'Restart'
>>> s.upper()
'RESTART'
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string
    
    Return a copy of the string S converted to uppercase.

>>> 
>>> 
>>> s = 'restart'.upper()
>>> print s
RESTART
>>> ================================ RESTART ================================
>>> 
>>> help(s.join)

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    help(s.join)
NameError: name 's' is not defined
>>> s = 'restart'.upper()
>>> help(s.join)
Help on built-in function join:

join(...)
    S.join(iterable) -> string
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

>>> s
'RESTART'
>>> s.join([' ', ' '])
' RESTART '
>>> s.join(['a ', ' b ', ' c'])
'a RESTART b RESTART c'
>>> help(s.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> s.center(20)
'      RESTART       '
>>> s.center(20, 'b')
'bbbbbbRESTARTbbbbbbb'
>>> '================================ RESTART ================================'
'================================ RESTART ================================'
>>> len('================================ RESTART ===============================')
72
>>> ' RESTART '
' RESTART '
>>> len(' RESTART ')
9
>>> s = 'restart'.upper()
>>> s
'RESTART'
>>> 'restart'.upper().center(9)
' RESTART '
>>> 
>>> 
>>> 'restart'.upper().center(9).center(72, '=')
'=============================== RESTART ================================'
>>> print 'restart'.upper().center(9).center(72, '=')
=============================== RESTART ================================
>>> ================================ RESTART ================================
>>> s = 'restart'.upper().center(9).center(72, '=')
>>> 
>>> 
>>> s
'=============================== RESTART ================================'
>>> ' '.join
<built-in method join of str object at 0x1080ebe18>
>>> ' '.join(['>>>', s])
'>>> =============================== RESTART ================================'
>>> print ' '.join(['>>>', s])
>>> =============================== RESTART ================================
>>> ================================ RESTART ================================
>>> s = 'restart'.upper().center(9).center(73, '=')
>>> print ' '.join(['>>>', s])
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
s = 'restart'.upper().center(9).center(73, '=')
>>> 
>>> LHS = '>>> '
>>> LHS + s
'>>> ================================ RESTART ================================'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> type(s)
<type 'str'>
>>> t = type(s)
>>> t
<type 'str'>
>>> help(t)
Help on class str in module __builtin__:

class str(basestring)
 |  str(object='') -> string
 |  
 |  Return a nice string representation of the object.
 |  If the argument is a string, the return value is the same object.
 |  
 |  Method resolution order:
 |      str
 |      basestring
 |      object
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> string
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getnewargs__(...)
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  capitalize(...)
 |      S.capitalize() -> string
 |      
 |      Return a copy of the string S with only its first character
 |      capitalized.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> string
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(...)
 |      S.decode([encoding[,errors]]) -> object
 |      
 |      Decodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |      as well as any other name registered with codecs.register_error that is
 |      able to handle UnicodeDecodeErrors.
 |  
 |  encode(...)
 |      S.encode([encoding[,errors]]) -> object
 |      
 |      Encodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that is able to handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs([tabsize]) -> string
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> string
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub [,start [,end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> string
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> string
 |      
 |      Return S left-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> string
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> string
 |      
 |      Return a copy of string S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub [,start [,end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub [,start [,end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> string
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string, starting at the end of the string and working
 |      to the front.  If maxsplit is given, at most maxsplit splits are
 |      done. If sep is not specified or is None, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  split(...)
 |      S.split([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are removed
 |      from the result.
 |  
 |  splitlines(...)
 |      S.splitlines(keepends=False) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  swapcase(...)
 |      S.swapcase() -> string
 |      
 |      Return a copy of the string S with uppercase characters
 |      converted to lowercase and vice versa.
 |  
 |  title(...)
 |      S.title() -> string
 |      
 |      Return a titlecased version of S, i.e. words start with uppercase
 |      characters, all remaining cased characters have lowercase.
 |  
 |  translate(...)
 |      S.translate(table [,deletechars]) -> string
 |      
 |      Return a copy of the string S, where all characters occurring
 |      in the optional argument deletechars are removed, and the
 |      remaining characters have been mapped through the given
 |      translation table, which must be a string of length 256 or None.
 |      If the table argument is None, no translation is applied and
 |      the operation simply removes the characters in deletechars.
 |  
 |  upper(...)
 |      S.upper() -> string
 |      
 |      Return a copy of the string S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> string
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width.  The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> 
>>> s = 'restart'.upper().center(9).center(73, '=')
>>> 
>>> s
'================================ RESTART ================================'
>>> 
>>> # Lunch from 12 to 1pm
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 'a, b, c, d, e'
'a, b, c, d, e'
>>> s = 'a, b, c, d, e'
>>> s
'a, b, c, d, e'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s.split()
['a,', 'b,', 'c,', 'd,', 'e']
>>> s
'a, b, c, d, e'
>>> 
>>> s = 'c, d, a, e, b
SyntaxError: EOL while scanning string literal
>>> s = 'c, d, a, e, b'
>>> s.split()
['c,', 'd,', 'a,', 'e,', 'b']
>>> 
>>> s.split(',')
['c', ' d', ' a', ' e', ' b']
>>> s.split(', ')
['c', 'd', 'a', 'e', 'b']
>>> s
'c, d, a, e, b'
>>> 
>>> 
>>> 
>>> 

>>> 
>>> s = 'This string has many words'
>>> s[0]
'T'
>>> s[:10]
'This strin'
>>> 
>>> 
>>> s[len(s) - 1]
's'
>>> s[-1]
's'
>>> 
>>> s[-10:]
'many words'
>>> s[3:5]
's '
>>> 
>>> s[:-10]
'This string has '
>>> 
>>> 
>>> s[-10]
'm'
>>> s
'This string has many words'
>>> len(s) - 10
16
>>> s[16]
'm'
>>> s[-10:19]
'man'
>>> 
>>> s[::2]
'Ti tighsmn od'
>>> 
>>> L = [1, 10, 7, 8, -3, -1]
>>> L
[1, 10, 7, 8, -3, -1]
>>> L[::2]
[1, 7, -3]
>>> L[::3]
[1, 8]
>>> L[::-1]
[-1, -3, 8, 7, 10, 1]
>>> s
'This string has many words'
>>> s[::-1]
'sdrow ynam sah gnirts sihT'
>>> 
>>> 
>>> s
'This string has many words'
>>> s + s
'This string has many wordsThis string has many words'
>>> 
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s = 'howdy'
>>> s * 2
'howdyhowdy'
>>> 
>>> s[:2] * 8
'hohohohohohohoho'
>>> 

>>> 
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> 
>>> s
'howdy'
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
>>> s + s
'howdyhowdy'
>>> s * 3
'howdyhowdyhowdy'
>>> 3 * s
'howdyhowdyhowdy'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> # On to Number Theory
>>> 
>>> 
>>> 
>>> a = 10
>>> a
10
>>> 
>>> # Numeric: int(bool, long), float, complex
>>> 
>>> type(2)
<type 'int'>
>>> type(2.0)
<type 'float'>
>>> type(2.)
<type 'float'>
>>> 2i
SyntaxError: invalid syntax
>>> 2j
2j
>>> type(2j)
<type 'complex'>
>>> 
>>> None = 10
SyntaxError: cannot assign to None
>>> 
>>> True
True
>>> False
False
>>> 
>>> OLD_TRUE = True
>>> True = 96.73
>>> True
96.73
>>> dir()
['OLD_TRUE', 'True', '__builtins__', '__doc__', '__name__', '__package__', 'a']
>>> 
>>> 
>>> del True
>>> dir()
['OLD_TRUE', '__builtins__', '__doc__', '__name__', '__package__', 'a']
>>> True
True
>>> 
>>> type(True)
<type 'bool'>
>>> type(False)
<type 'bool'>
>>> True = 96.73
>>> type(True)
<type 'float'>
>>> bool(True)
True
>>> True
96.73
>>> True bool(True)
SyntaxError: invalid syntax
>>> True = bool(1.0)
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
>>> true

Traceback (most recent call last):
  File "<pyshell#468>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> None
>>> __name__
'__main__'
>>> 
>>> __package__
>>> print __package__
None
>>> __package__ is None
True
>>> __builtins__
<module '__builtin__' (built-in)>
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> long
<type 'long'>
>>> long(2)
2L
>>> 2
2
>>> 
>>> 
>>> 

>>> 2**63 - 1
9223372036854775807L
>>> 9223372036854775807
9223372036854775807
>>> 9223372036854775807 + 1
9223372036854775808L
>>> 
>>> 
>>> 
>>> 3 ^ 5
6
>>> # 3 = 2 + 1
>>> # 5 = 4 + 1
>>> # XOR: 3 ^ 5 = 4 + 2
>>> 
>>> dir(3)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 3 | 5
7
>>> 3 & 5
1
>>> 
>>> 
>>> 
>>> 
>>> s = '1, 2, 3, 4, 5'
>>> s.split(', ')
['1', '2', '3', '4', '5']
>>> 
>>> type(2)
<type 'int'>
>>> int('1')
1
>>> int('9223372036854775807')
9223372036854775807
>>> int('9223372036854775808')
9223372036854775808L
>>> help(int)
Help on class int in module __builtin__:

class int(object)
 |  int(x=0) -> int or long
 |  int(x, base=10) -> int or long
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is floating point, the conversion truncates towards zero.
 |  If x is outside the integer range, the function returns a long instead.
 |  
 |  If x is not a number or if base is given, then x must be a string or
 |  Unicode object representing an integer literal in the given base.  The
 |  literal can be preceded by '+' or '-' and be surrounded by whitespace.
 |  The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
 |  interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(...)
 |      x.__abs__() <==> abs(x)
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __and__(...)
 |      x.__and__(y) <==> x&y
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __coerce__(...)
 |      x.__coerce__(y) <==> coerce(x, y)
 |  
 |  __div__(...)
 |      x.__div__(y) <==> x/y
 |  
 |  __divmod__(...)
 |      x.__divmod__(y) <==> divmod(x, y)
 |  
 |  __float__(...)
 |      x.__float__() <==> float(x)
 |  
 |  __floordiv__(...)
 |      x.__floordiv__(y) <==> x//y
 |  
 |  __format__(...)
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getnewargs__(...)
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __hex__(...)
 |      x.__hex__() <==> hex(x)
 |  
 |  __index__(...)
 |      x[y:z] <==> x[y.__index__():z.__index__()]
 |  
 |  __int__(...)
 |      x.__int__() <==> int(x)
 |  
 |  __invert__(...)
 |      x.__invert__() <==> ~x
 |  
 |  __long__(...)
 |      x.__long__() <==> long(x)
 |  
 |  __lshift__(...)
 |      x.__lshift__(y) <==> x<<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(y) <==> x*y
 |  
 |  __neg__(...)
 |      x.__neg__() <==> -x
 |  
 |  __nonzero__(...)
 |      x.__nonzero__() <==> x != 0
 |  
 |  __oct__(...)
 |      x.__oct__() <==> oct(x)
 |  
 |  __or__(...)
 |      x.__or__(y) <==> x|y
 |  
 |  __pos__(...)
 |      x.__pos__() <==> +x
 |  
 |  __pow__(...)
 |      x.__pow__(y[, z]) <==> pow(x, y[, z])
 |  
 |  __radd__(...)
 |      x.__radd__(y) <==> y+x
 |  
 |  __rand__(...)
 |      x.__rand__(y) <==> y&x
 |  
 |  __rdiv__(...)
 |      x.__rdiv__(y) <==> y/x
 |  
 |  __rdivmod__(...)
 |      x.__rdivmod__(y) <==> divmod(y, x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rfloordiv__(...)
 |      x.__rfloordiv__(y) <==> y//x
 |  
 |  __rlshift__(...)
 |      x.__rlshift__(y) <==> y<<x
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(y) <==> y*x
 |  
 |  __ror__(...)
 |      x.__ror__(y) <==> y|x
 |  
 |  __rpow__(...)
 |      y.__rpow__(x[, z]) <==> pow(x, y[, z])
 |  
 |  __rrshift__(...)
 |      x.__rrshift__(y) <==> y>>x
 |  
 |  __rshift__(...)
 |      x.__rshift__(y) <==> x>>y
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rtruediv__(...)
 |      x.__rtruediv__(y) <==> y/x
 |  
 |  __rxor__(...)
 |      x.__rxor__(y) <==> y^x
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __truediv__(...)
 |      x.__truediv__(y) <==> x/y
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(...)
 |      x.__xor__(y) <==> x^y
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> int('111', 2)
7
>>> int('deadbeef', 16)
3735928559
>>> int('ff', 16)
255
>>> 
>>> 2**63 - 1
9223372036854775807L
>>> '1' * 63
'111111111111111111111111111111111111111111111111111111111111111'
>>> 
>>> int('1' * 63, 2)
9223372036854775807
>>> int('1' * 63, 2) + 1
9223372036854775808L
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> # Philosophy
>>> # What is truth?
>>> # What does it mean to be "True"?
>>> 
>>> 
>>> 96.73
96.73
>>> 
>>> # 1. Not equal to zero
>>> 
>>> # 2. Not None
>>> # 3. Don't be empty
>>> 
>>> 
>>> # Container types
>>> L = [1, 7, -10]
>>> bool(L)
True
>>> []
[]
>>> bool([])
False
>>> 
>>> 
>>> 
>>> # list, tuple, dictionary, set
>>> 
>>> L = [1, -10, 7]
>>> T = (1, 4, 5)
>>> T
(1, 4, 5)
>>> L
[1, -10, 7]
>>> type(L)
<type 'list'>
>>> type(T)
<type 'tuple'>
>>> 
>>> L[0]
1
>>> T[0]
1
>>> help(T)
Help on tuple object:

class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getnewargs__(...)
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> dir(T)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> len(dir(L))
45
>>> len(dir(T))
32
>>> 
>>> dir(L) - dir(T)

Traceback (most recent call last):
  File "<pyshell#578>", line 1, in <module>
    dir(L) - dir(T)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> 
>>> 
>>> S = set([1, 4, 5])
>>> S
set([1, 4, 5])
>>> set([1, 4, 5]) - set([1, 5, 6])
set([4])
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(T)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> set(dir(L)) - set(dir(T))
set(['sort', 'insert', '__reversed__', '__delslice__', 'reverse', 'extend', '__delitem__', '__setslice__', 'remove', '__setitem__', '__iadd__', 'pop', 'append', '__imul__'])
>>> help(L.sort)
Help on built-in function sort:

sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1

>>> L
[1, -10, 7]
>>> L.sort()
>>> L
[-10, 1, 7]
'
>>> T.sort

Traceback (most recent call last):
  File "<pyshell#591>", line 1, in <module>
    T.sort
AttributeError: 'tuple' object has no attribute 'sort'
>>> sorted(T)
[1, 4, 5]
>>> 
>>> xyzt

Traceback (most recent call last):
  File "<pyshell#594>", line 1, in <module>
    xyzt
NameError: name 'xyzt' is not defined
>>> 
>>> 
>>> 
>>> set(dir(T)) - set(dir(L))
set(['__getnewargs__'])
>>> 
>>> 

>>> 
>>> 
>>> s = set([1, 2, 3])
>>> s = {1, 2, 3}
>>> s
set([1, 2, 3])
>>> 
>>> 
>>> D = {1: 3, 5: 10, 11: -6}
>>> D
{1: 3, 11: -6, 5: 10}
>>> 
>>> 
>>> 
>>> 
>>> D
{1: 3, 11: -6, 5: 10}
>>> 
>>> dir(D)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> 
>>> help(D.get)
Help on built-in function get:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

>>> 
>>> 
>>> 
>>> D.get
<built-in method get of dict object at 0x10c45e050>
>>> D
{1: 3, 11: -6, 5: 10}
>>> D.get(11)
-6
>>> 
>>> 

>>> D[11]
-6
>>> D[110]

Traceback (most recent call last):
  File "<pyshell#628>", line 1, in <module>
    D[110]
KeyError: 110
>>> 
>>> 
>>> 

>>> D.get
<built-in method get of dict object at 0x10c45e050>
>>> help(D.get)
Help on built-in function get:

get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

>>> D.get(110)
>>> D[110]

Traceback (most recent call last):
  File "<pyshell#635>", line 1, in <module>
    D[110]
KeyError: 110
>>> print D.get(110)
None
>>> D.get(110, 42)
42
>>> 
>>> 
>>> D
{1: 3, 11: -6, 5: 10}
>>> D[None] = 48
>>> D
{1: 3, 11: -6, 5: 10, None: 48}
>>> D['s'] = (7, 8, 9)
>>> D
{1: 3, 's': (7, 8, 9), 11: -6, 5: 10, None: 48}
>>> D[True] = D
>>> 
>>> D
{1: {...}, 's': (7, 8, 9), 11: -6, 5: 10, None: 48}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> L
[-10, 1, 7]
>>> D[L] = 90

Traceback (most recent call last):
  File "<pyshell#655>", line 1, in <module>
    D[L] = 90
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> T
(1, 4, 5)
>>> D[T] = 90
>>> D
{1: {...}, 5: 10, 11: -6, (1, 4, 5): 90, 's': (7, 8, 9), None: 48}
>>> 
>>> 
>>> dir(D)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> 
>>> 
>>> D.clear()
>>> D
{}
>>> 
>>> 
>>> 
>>> 
>>> 1 == 1
True
>>> 1 == 1.0
True
>>> 'sa' == 'sa
SyntaxError: EOL while scanning string literal
>>> 'sa' == 'sa'
True
>>> 
>>> 1 < 's'
True
>>> 's' < 1
False
>>> 
>>> '\x01'
'\x01'
>>> '1'
'1'
>>> 
>>> 
>>> 
>>> 
>>> dir(1)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> cmp(1, 's')
-1
>>> cmp(1, 1)
0
>>> cmp('s', 1)
1
>>> 
>>> 
>>> class Foo:
	"""Hi foo"""

	
>>> class Bar:
	"""Hi bar"""

	
>>> f = Foo()
>>> b = Bar()
>>> b < f
True
>>> f < b
False
>>> 
>>> 
>>> 
>>> x = 1
>>> y = 1
>>> x is y
True
>>> a = []
>>> b = []
>>> a is b
False
>>> a
[]
>>> id(a)
4499871720
>>> hex(id(a))
'0x10c3697e8'
>>> f
<__main__.Foo instance at 0x10c36b518>
>>> hex(id(f))
'0x10c36b518'
>>> hex(id(b))
'0x10c241ea8'
>>> x
1
>>> y
1
>>> # WAT
>>> 
>>> 
>>> 
>>> 
>>> # JavaScript WAT: 1 + '1'
>>> 1 + '1'

Traceback (most recent call last):
  File "<pyshell#731>", line 1, in <module>
    1 + '1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> x is y
  File "<pyshell#735>", line 1
    is y
    ^
IndentationError: unexpected indent
>>> x is y
True
>>> 
>>> 
>>> 
>>> x = 4000
>>> y = 4000
>>> x is y
False
>>> 
>>> 
>>> 
>>> a = [1, 3, 10]
>>> b = a
>>> a is b
True
>>> 
>>> 
>>> b.append('T')
>>> b
[1, 3, 10, 'T']
>>> a isb
SyntaxError: invalid syntax
>>> a is b
True
>>> 
>>> a
[1, 3, 10, 'T']
>>> 
>>> 
>>> # BREAK: 2:04pm to 2:14pm
>>> 
>>> # 10 // 7
>>> 
>>> 
>>> x = 1
>>> y = x
>>> x
1
>>> y
1
>>> x = 4000
>>> y = x
>>> x is y
True
>>> x
4000
>>> y
4000
>>> x == y
True
>>> y is x
True
>>> x
4000
>>> y
4000
>>> y = 5000
>>> x
4000
>>> 
>>> 
>>> x = 4000
>>> ================================ RESTART ================================
>>> 
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> x = 4000
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> x
4000
>>> y = x
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'x', 'y']
>>> id(x)
140439673687736
i
>>> 
>>> id(y)
140439673687736
>>> y = 5000
>>> 
>>> D = {1: 5}
>>> 
>>> 
>>> 
>>> # How do I check if a number is between -1 and 1
>>> x = 0.4
>>> if x > -1:
	if x < 1:
		print 'Yay I win'

		
Yay I win
>>> x = 1.4
>>> if x > -1:
	if x < 1:
		print 'Yay I win'

		
>>> if -1 < x < 1:
	print 'Yay I win'

	
>>> x = 0.4
>>> if -1 < x < 1:
	print 'Yay I win'
else:
	print 'Oh noes I lose'

	
Yay I win
>>> if -1 < x < 1:
	print 'Yay I win'
elif 1 < x < 2:
	print 'So close.'
else:
	print 'Oh noes I lose'

	
Yay I win
>>> x = 1.4
>>> if -1 < x < 1:
	print 'Yay I win'
elif 1 < x < 2:
	print 'So close.'
else:
	print 'Oh noes I lose'

	
So close.
>>> x = 2.4
>>> if -1 < x < 1:
	print 'Yay I win'
elif 1 < x < 2:
	print 'So close.'
else:
	print 'Oh noes I lose'

	
Oh noes I lose
>>> 
>>> 
>>> s = 'abc'
>>> for attribute in dir(s):
	print attribute

	
__add__
__class__
__contains__
__delattr__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__getslice__
__gt__
__hash__
__init__
__le__
__len__
__lt__
__mod__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
_formatter_field_name_split
_formatter_parser
capitalize
center
count
decode
encode
endswith
expandtabs
find
format
index
isalnum
isalpha
isdigit
islower
isspace
istitle
isupper
join
ljust
lower
lstrip
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
>>> 
>>> 
>>> D = {10: 1, 9: -4, 'a': 'b'}
>>> D
{'a': 'b', 9: -4, 10: 1}
>>> dir(D)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> 
>>> 
>>> for k in D.keys():
	print k

	
a
9
10
>>> for k in D.keys():
	print k

	
a
9
10
>>> 
>>> L = ['a', 10, None]
>>> for thing in L:
	print thing

	
a
10
None
>>> 
>>> 
>>> for thing in D:
	print thing

	
a
9
10
>>> D
{'a': 'b', 9: -4, 10: 1}
>>> 
>>> 
>>> for v in D.values():
	print v

	
b
-4
1
>>> D
{'a': 'b', 9: -4, 10: 1}
>>> 
>>> for item in D.items():
	print item

('a', 'b')
(9, -4)
(10, 1)
>>> item
(10, 1)
>>> type(item)
<type 'tuple'>
>>> 
>>> item[0]
10
>>> item[1]
1
>>> for item in D.items():
	print item[0], '-->', item[1]

	
a --> b
9 --> -4
10 --> 1
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> for k, v in D.items():
	print k, '-->', v

	
a --> b
9 --> -4
10 --> 1
>>> 
>>> D.items()
[('a', 'b'), (9, -4), (10, 1)]
>>> list(D.items())
[('a', 'b'), (9, -4), (10, 1)]
>>> type(D.items())
<type 'list'>
>>> k, v = 'Batman', 'Robin'
>>> k
'Batman'
>>> b

Traceback (most recent call last):
  File "<pyshell#883>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> v
'Robin'
>>> T = ('Batman', 'Robin')
>>> T
('Batman', 'Robin')
>>> type(T)
<type 'tuple'>
>>> k, v = T
>>> 
>>> 
>>> 
>>> T = ('Batman',)
>>> T
('Batman',)
>>> T = ('Batman')
>>> T
'Batman'
>>> T = ('Batman',)
>>> T
('Batman',)
>>> k, v = T

Traceback (most recent call last):
  File "<pyshell#898>", line 1, in <module>
    k, v = T
ValueError: need more than 1 value to unpack
>>> T = ('Batman', 'Robin', 'Alfred')
>>> k, v = T

Traceback (most recent call last):
  File "<pyshell#900>", line 1, in <module>
    k, v = T
ValueError: too many values to unpack
>>> 
>>> T[0]
'Batman'
>>> T[1]
'Robin'
>>> k, v, _ = T
>>> k, v, _ = 'Batman', 'Robin', 'Alfred'
>>> k
'Batman'
>>> v
'Robin'
>>> dir()
['D', 'L', 'T', '_', '__builtins__', '__doc__', '__name__', '__package__', 'attribute', 'item', 'k', 's', 'thing', 'this', 'v', 'x', 'y']
>>> _
'Alfred'
>>> matches = [5, 6]
>>> match, = matches

Traceback (most recent call last):
  File "<pyshell#911>", line 1, in <module>
    match, = matches
ValueError: too many values to unpack
>>> matches = [5]
>>> match, = matches
>>> match
5
>>> 
>>> 
>>> 
>>> L = ['1'] * 10
>>> L
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
>>> k, v, _ = L

Traceback (most recent call last):
  File "<pyshell#920>", line 1, in <module>
    k, v, _ = L
ValueError: too many values to unpack
>>> k, v, _, _, _, _, _, _, _, _ = L
>>> L = list('0123456789')
>>> L
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> k, v, _, _, _, _, _, _, _, _ = L
>>> k
'0'
>>> v
'1'
>>> _
'9'
>>> 
>>> T = ('Batman', 'Robin')
>>> 
>>> 
>>> 
>>> 
>>> D = {'Donatello': 'Bo',
         'Michaelangelo': 'Nunchuk',
         'Leonardo': 'Katana',
         'Rafael': 'Sai'}
>>> 
>>> D
{'Leonardo': 'Katana', 'Donatello': 'Bo', 'Michaelangelo': 'Nunchuk', 'Rafael': 'Sai'}
>>> 
>>> for k, v in D.items():
	print k, v

	
Leonardo Katana
Donatello Bo
Michaelangelo Nunchuk
Rafael Sai
>>> 
>>> 
>>> for turle, weapon in D.items():
	print turtle, weapon

	

Traceback (most recent call last):
  File "<pyshell#949>", line 2, in <module>
    print turtle, weapon
NameError: name 'turtle' is not defined
>>> for turtle, weapon in D.items():
	print turtle, weapon

	
Leonardo Katana
Donatello Bo
Michaelangelo Nunchuk
Rafael Sai
>>> 
>>> message = turtle + ' yields a ' + weapon
>>> message
'Rafael yields a Sai'
>>> message = '%s yields a %s' % (turtle, weapon)
>>> message
'Rafael yields a Sai'
>>> for turtle, weapon in D.items():
	print '%s yields a %s' % (turtle, weapon)

	
Leonardo yields a Katana
Donatello yields a Bo
Michaelangelo yields a Nunchuk
Rafael yields a Sai
>>> 
>>> len('Michaelangelo')
13
>>> for turtle, weapon in D.items():
	print '%13s yields a %s' %
# IndentationError: ('unindent does not match any outer indentation level', ('<tokenize>', 2639, 5, '     Leonardo yields a Katana\n'))

# IndentationError: ('unindent does not match any outer indentation level', ('<tokenize>', 5, 4, '    Donatello yields a Bo\n'))
turtle, weapon)

	
     Leonardo yields a Katana
    Donatello yields a Bo
Michaelangelo yields a Nunchuk
       Rafael yields a Sai
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()
'/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace'
>>> ================================ RESTART ================================
>>> 
====== Source: http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt ======
                      Starting download at Mon Dec  7 14:43:39 2015                       
http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt
200  OK           http://www.bossylobster.com/learning-python/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (current) 
200  OK           http://www.bossylobster.com/learning-python/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (current) 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
>>> # 2:45pm, open vcard.py
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__']
>>> __file__
'/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard.py'
>>> 
>>> __name__
'__main__'
>>> __doc__
'Script for making vCards.\n\nMaking vCards (with QR codes) for brother-in-law.\nRaisin Company is pretend.\n'
>>> print __doc__
Script for making vCards.

Making vCards (with QR codes) for brother-in-law.
Raisin Company is pretend.

>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> import os
>>> os.listdir('.')
['day1.idle.py', 'download.py', 'highlight.py', 'highlight.pyc', 'index.html.template', 'links.txt', 'module.html.template', 'notes', 'notes.txt', 'publish.py', 'read_python.py', 'vcard.py']
>>> os.listdir('notes')
['etag_db.bak', 'etag_db.dat', 'etag_db.dir', 'PythonAwesome.pdf', 'raisin_team.csv']
>>> 
>>> 
>>> open
<built-in function open>
>>> help(open)
Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

>>> ================================ RESTART ================================
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'f', 'filename']
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x1041419c0>
>>> filename
'notes/raisin_team.csv'
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x1041419c0>
>>> type(f)
<type 'file'>
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300

Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318

Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348

Jones,David,Grape Ager,david@example.com,559-555-2379

Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301

Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333

Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397

Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565

Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513

Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> 
>>> 
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> 
>>> 
>>> print 'a\tb\ncfg'
a	b
cfg
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> print line
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> 
>>> line[:-1]
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> dir(line)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> line.strip
<built-in method strip of str object at 0x1088ffce0>
>>> help(line.strip)
Help on built-in function strip:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> line.strip()
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> print line.strip()
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> print line,
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> print 'abc',
abc
>>> ================================ RESTART ================================
>>> 
abc def
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
>>> 
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x1068939c0>
>>> f.close
<built-in method close of file object at 0x1068939c0>
>>> help(f.close)
Help on built-in function close:

close(...)
    close() -> None or (perhaps) an integer.  Close the file.
    
    Sets data attribute .closed to True.  A closed file cannot be used for
    further I/O operations.  close() may be called more than once without
    error.  Some kinds of file objects (for example, opened by popen())
    may return an exit status upon closing.

>>> 
>>> 
>>> f.close()
SyntaxError: invalid syntax
>>> 
>>> f.close()
>>> 
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x1068939c0>
>>> 
>>> 
>>> k, v = 'batman', 'robin', 'alfred'

Traceback (most recent call last):
  File "<pyshell#1032>", line 1, in <module>
    k, v = 'batman', 'robin', 'alfred'
ValueError: too many values to unpack
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
>>> 
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x1106419c0>
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard.py", line 11, in <module>
    k, v = 'batman', 'robin', 'alfred'
ValueError: too many values to unpack
>>> 
>>> f
<open file 'notes/raisin_team.csv', mode 'r' at 0x10bace9c0>
>>> ================================ RESTART ================================
>>> 
Oh noes, we got an error
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x108e81f60>
>>> 1 / 0

Traceback (most recent call last):
  File "<pyshell#1039>", line 1, in <module>
    1 / 0
ZeroDivisionError: integer division or modulo by zero
>>> L = [1, 2]
>>> L[10]

Traceback (most recent call last):
  File "<pyshell#1041>", line 1, in <module>
    L[10]
IndexError: list index out of range
>>> D ={}
>>> D[10]

Traceback (most recent call last):
  File "<pyshell#1043>", line 1, in <module>
    D[10]
KeyError: 10
>>> ================================ RESTART ================================
>>> 
This is the finally statement

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard.py", line 12, in <module>
    k, v = 'batman', 'robin', 'alfred'
ValueError: too many values to unpack
>>> 
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x10bc889c0>
>>> ================================ RESTART ================================
>>> 
I got an error
>>> ================================ RESTART ================================
>>> 
I got an error
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x10582d9c0>
>>> 
>>> 
>>> 2 + 4
6
>>> (2).__add__(4)
6
>>> 
>>> dir(f)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard.py", line 11, in <module>
    k, v = 'batman', 'robin', 'alfred'
ValueError: too many values to unpack
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x1059419c0>
>>> 
>>> import threading
>>> threading.Lock
<built-in function allocate_lock>
>>> 
>>> 
>>> lock = threading.Lock()
>>> dir(lock)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'acquire', 'acquire_lock', 'locked', 'locked_lock', 'release', 'release_lock']
>>> lock.locked
<built-in method locked of thread.lock object at 0x1049049d0>
>>> lock.locked()
False
>>> 
>>> 
>>> with lock:
	print lock.locked()

	
True
>>> lock.locked()
False
>>> 
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
>>> 
>>> 
>>> try:
	a = 1/0
finally:
	print "I'm done"

	
I'm done

Traceback (most recent call last):
  File "<pyshell#1079>", line 2, in <module>
    a = 1/0
ZeroDivisionError: integer division or modulo by zero
>>> try:
	a = 1/0
except:
	print 'I caught anything in the world'

I caught anything in the world
>>> 
>>> try:
	a = 1/0
except:
	print 'I caught'
finally:
	print 'I cleaned up, rain or shine'

	
I caught
I cleaned up, rain or shine
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> 
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> line.split
<built-in method split of str object at 0x10659fce0>
>>> line.split(',')
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700\n']
>>> line.strip()
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> help(line.strip)
Help on built-in function strip:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> '\n\t     \r   f  \n \r\n'.strip()
'f'
>>> '\n\t     \r   f  \n \r\n'.rstrip()
'\n\t     \r   f'
>>> help(line.strip)
Help on built-in function strip:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> str
<type 'str'>
>>> str.strip
<method 'strip' of 'str' objects>
>>> help(str.strip)
Help on method_descriptor:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> 
>>> help(line)
no Python documentation found for 'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'

>>> help(str)
Help on class str in module __builtin__:

class str(basestring)
 |  str(object='') -> string
 |  
 |  Return a nice string representation of the object.
 |  If the argument is a string, the return value is the same object.
 |  
 |  Method resolution order:
 |      str
 |      basestring
 |      object
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> string
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getnewargs__(...)
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mod__(...)
 |      x.__mod__(y) <==> x%y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmod__(...)
 |      x.__rmod__(y) <==> y%x
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  capitalize(...)
 |      S.capitalize() -> string
 |      
 |      Return a copy of the string S with only its first character
 |      capitalized.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> string
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(...)
 |      S.decode([encoding[,errors]]) -> object
 |      
 |      Decodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
 |      as well as any other name registered with codecs.register_error that is
 |      able to handle UnicodeDecodeErrors.
 |  
 |  encode(...)
 |      S.encode([encoding[,errors]]) -> object
 |      
 |      Encodes S using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that is able to handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs([tabsize]) -> string
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> string
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub [,start [,end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> string
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> string
 |      
 |      Return S left-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> string
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> string
 |      
 |      Return a copy of string S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub [,start [,end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub [,start [,end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> string
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string, starting at the end of the string and working
 |      to the front.  If maxsplit is given, at most maxsplit splits are
 |      done. If sep is not specified or is None, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  split(...)
 |      S.split([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in the string S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are removed
 |      from the result.
 |  
 |  splitlines(...)
 |      S.splitlines(keepends=False) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> string or unicode
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is unicode, S will be converted to unicode before stripping
 |  
 |  swapcase(...)
 |      S.swapcase() -> string
 |      
 |      Return a copy of the string S with uppercase characters
 |      converted to lowercase and vice versa.
 |  
 |  title(...)
 |      S.title() -> string
 |      
 |      Return a titlecased version of S, i.e. words start with uppercase
 |      characters, all remaining cased characters have lowercase.
 |  
 |  translate(...)
 |      S.translate(table [,deletechars]) -> string
 |      
 |      Return a copy of the string S, where all characters occurring
 |      in the optional argument deletechars are removed, and the
 |      remaining characters have been mapped through the given
 |      translation table, which must be a string of length 256 or None.
 |      If the table argument is None, no translation is applied and
 |      the operation simply removes the characters in deletechars.
 |  
 |  upper(...)
 |      S.upper() -> string
 |      
 |      Return a copy of the string S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> string
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width.  The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> 
>>> 
>>> line.strip()
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> line.strip().split(',')
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
>>> ================================ RESTART ================================
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'data', 'f', 'line']
>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x1081c19c0>
>>> 
>>> 
>>> |      Return a list of the lines in S, breaking at line boundaries.
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> weird_spaces = 'a  \t\n      b    \t\r    c   '
>>> weird_spaces.split()
['a', 'b', 'c']
>>> weird_spaces = 'a  \t\n    ,  b    \t\r,    c   '
>>> weird_spaces.split(',')
['a  \t\n    ', '  b    \t\r', '    c   ']
>>> 
>>> 
>>> data
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
>>> data = []
>>> data[0]

Traceback (most recent call last):
  File "<pyshell#1137>", line 1, in <module>
    data[0]
IndexError: list index out of range
>>> data = ['a', 'b']
>>> data[4]

Traceback (most recent call last):
  File "<pyshell#1139>", line 1, in <module>
    data[4]
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
>>> last_name
'Schmidt'
>>> first_name
'Gertrude'
>>> title
'VP Business Development'
>>> email
'gertrude@example.com'
>>> phone
'559-555-6700'
>>> 
>>> s = 'abc'
>>> first, second, third = s
>>> first
'a'
>>> second
'b'
t
>>> third
'c'
>>> a, b = '1', '2', '3'

Traceback (most recent call last):
  File "<pyshell#1151>", line 1, in <module>
    a, b = '1', '2', '3'
ValueError: too many values to unpack
>>> ================================ RESTART ================================
>>> 
>>> 
>>> '%s -> %s' % ('hi', 'bye')
'hi -> bye'
>>> 
>>> # Break 3:31pm to 3:41pm
>>> ================================ RESTART ================================
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> VCARD_TEMPLATE
'\nBEGIN:VCARD\nVERSION:2.1\nN:%s;%s\nFN:%s\nORG:California Raisin Company\nTITLE:%s\nTEL;WORK;VOICE:%s\nADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America\nEMAIL;PREF;INTERNET:%s\nEND:VCARD\n'
>>> ================================ RESTART ================================
>>> 
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:California Raisin Company
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:raymond@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:California Raisin Company
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:mary@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:California Raisin Company
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:harold@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:California Raisin Company
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:martin@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:California Raisin Company
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:david@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:California Raisin Company
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:luis@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:California Raisin Company
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2333
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:fritz@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:California Raisin Company
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:esmerelda@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:California Raisin Company
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-6565
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:marilyn@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:California Raisin Company
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:blair@example.com
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:California Raisin Company
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America
EMAIL;PREF;INTERNET:gertrude@example.com
END:VCARD

>>> last_name
'Schmidt'
f
>>> first_name
'Gertrude'
>>> ================================ RESTART ================================
>>> 
Raymond.Hettinger.vcf
Mary.Thomas.vcf
Harold.Davis.vcf
Martin.Masterson.vcf
David.Jones.vcf
Luis.Zapata.vcf
Fritz.Gunter.vcf
Esmerela.Pichon.vcf
Marilyn.Blain.vcf
Blair.Marks.vcf
Gertrude.Schmidt.vcf
>>> 
>>> 
>>> 
>>> 
>>> help(open)
Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x10cfc19c0>
>>> print file.__doc__
file(name[, mode[, buffering]]) -> file object

Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files.
Add a '+' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.  The preferred way
to open a file is with the builtin open() function.
Add a 'U' to mode to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a '\n'
in Python.  Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
'\r', '\n', '\r\n' or a tuple containing all the newline types seen.

'U' cannot be combined with 'w' or '+' mode.

>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> VCARD_TEMPLATE
'BEGIN:VCARD\nVERSION:2.1\nN:%s;%s\nFN:%s\nORG:California Raisin Company\nTITLE:%s\nTEL;WORK;VOICE:%s\nADR;WORK:;;123 Fake Street;Jan Sose;CA;95111;United States of America\nEMAIL;PREF;INTERNET:%s\nEND:VCARD\n'
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond.Hettinger.vcf to disk
Just wrote Mary.Thomas.vcf to disk
Just wrote Harold.Davis.vcf to disk
Just wrote Martin.Masterson.vcf to disk
Just wrote David.Jones.vcf to disk
Just wrote Luis.Zapata.vcf to disk
Just wrote Fritz.Gunter.vcf to disk
Just wrote Esmerela.Pichon.vcf to disk
Just wrote Marilyn.Blain.vcf to disk
Just wrote Blair.Marks.vcf to disk
Just wrote Gertrude.Schmidt.vcf to disk
>>> 
>>> 
>>> import qr

Traceback (most recent call last):
  File "<pyshell#1172>", line 1, in <module>
    import qr
ImportError: No module named qr
>>> import qrcode

Traceback (most recent call last):
  File "<pyshell#1173>", line 1, in <module>
    import qrcode
ImportError: No module named qrcode
>>> 
>>> 
>>> # Requirements to be in Python's standard library
>>> # stdlib
>>> 
>>> # 1. useful to everyone
>>> # 2. bugs
>>> # 2. NO bugs
>>> # 3. no unsolved reproducible issues
>>> # 4. stable
>>> # 1. GENERAL PURPOSE
>>> 
>>> 
>>> s = 'abc'
>>> s.strip
<built-in method strip of str object at 0x1005d98f0>
>>> # https://goo.gl/a1igSR
>>> ord('+')
43
>>> hex(ord('+'))
'0x2b'
>>> 
>>> 
>>> 
>>> URL = 'https://chart.googleapis.com/chart?cht=qr&chl=Hello+World&choe=UTF-8&chs=300x300'
>>> 
>>> URL
'https://chart.googleapis.com/chart?cht=qr&chl=Hello+World&choe=UTF-8&chs=300x300'
>>> 
>>> import http

Traceback (most recent call last):
  File "<pyshell#1199>", line 1, in <module>
    import http
ImportError: No module named http
>>> import
SyntaxError: invalid syntax
>>> import urrlib

Traceback (most recent call last):
  File "<pyshell#1201>", line 1, in <module>
    import urrlib
ImportError: No module named urrlib
>>> 
>>> 
>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_asciire', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', '_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'always_safe', 'base64', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'noheaders', 'os', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 'quote_plus', 're', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test1', 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
>>> 
>>> URL
'https://chart.googleapis.com/chart?cht=qr&chl=Hello+World&choe=UTF-8&chs=300x300'
>>> 
>>> # Make a connection
>>> cnxn = urllib.urlopen(URL)
>>> data = cnxn.read()
>>> cnxn.close()
>>> # import urllib
>>> len(data)
1274
>>> data[:10]
'\x89PNG\r\n\x1a\n\x00\x00'
>>> 
>>> 
>>> with open('hello_world.png', 'w') as png_file:
	png_file.write(data)

	
>>> dir(cnxn)
['__doc__', '__init__', '__iter__', '__module__', '__repr__', 'close', 'code', 'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'next', 'read', 'readline', 'readlines', 'url']
>>> 
>>> 
>>> URL
'https://chart.googleapis.com/chart?cht=qr&chl=Hello+World&choe=UTF-8&chs=300x300'
>>> 
>>> 
>>> a = """first
second
third"""
>>> a
'first\nsecond\nthird'
>>> print a
first
second
third
>>> b = ('first'
         'second'
         'third')
>>> b
'firstsecondthird'
>>> 

>>> 
>>> '%s goodbye' % 'foo'
'foo goodbye'
>>> '%s goodbye' % ('foo',)
'foo goodbye'
>>> '%s goodbye %s' % ('foo', 'bar')
'foo goodbye bar'
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond.Hettinger.vcf to disk

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard.py", line 41, in <module>
    cnxn = urllib.urlopen(vcard_url)
NameError: name 'urllib' is not defined
>>> ZZTOP

Traceback (most recent call last):
  File "<pyshell#1243>", line 1, in <module>
    ZZTOP
NameError: name 'ZZTOP' is not defined
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond.Hettinger.vcf to disk
Just wrote Mary.Thomas.vcf to disk
Just wrote Harold.Davis.vcf to disk
Just wrote Martin.Masterson.vcf to disk
Just wrote David.Jones.vcf to disk
Just wrote Luis.Zapata.vcf to disk
Just wrote Fritz.Gunter.vcf to disk
Just wrote Esmerela.Pichon.vcf to disk
Just wrote Marilyn.Blain.vcf to disk
Just wrote Blair.Marks.vcf to disk
Just wrote Gertrude.Schmidt.vcf to disk
>>> 
>>> 
>>> 
>>> data[:10]
'\x89PNG\r\n\x1a\n\x00\x00'
>>> 0x89
137
>>> 
>>> ord('\n')
10
>>> 0x0a
10
>>> chr(0x0a)
'\n'
>>> 
>>> 
>>> 
>>> 
>>> print file.__doc__
file(name[, mode[, buffering]]) -> file object

Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files.
Add a '+' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.  The preferred way
to open a file is with the builtin open() function.
Add a 'U' to mode to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a '\n'
in Python.  Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
'\r', '\n', '\r\n' or a tuple containing all the newline types seen.

'U' cannot be combined with 'w' or '+' mode.

>>> f
<closed file 'notes/raisin_team.csv', mode 'r' at 0x102d216f0>
>>> f.newlines
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> 
>>> # 4:43pm, create vcard_update.py
>>> ================================ RESTART ================================
>>> 
====== Source: http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt ======
                      Starting download at Mon Dec  7 16:46:31 2015                       
http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt
200  OK           http://www.bossylobster.com/learning-python/shared/raisin_team_update.csv
                  --> notes/raisin_team_update.csv (updated) 
200  OK           http://www.bossylobster.com/learning-python/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (current) 
200  OK           http://www.bossylobster.com/learning-python/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (current) 
>>> ================================ RESTART ================================
>>> 
"Hettinger","Raymond","VP Raisin Smushing","raymond@example.com","559-555-1212"
"Thomas","Mary","Sr. Associate Raisin Design","mary@example.com","559-555-2300"
"Davis","Harold","Chief Raisin Picker","harold@example.com","559-555-2318"
"Masterson","Martin","Asst Raisin Smusher","martin@example.com","559-555-2348"
"Jones","David","Grape Ager","david@example.com","559-555-2379"
"Zapata","Luis","VP Grape Sales","luis@example.com","559-555-2301"
"Gunter","Fritz","Grape Smusher","fritz@example.com","559-555-2333"
"Pichon","Esmerela","Head Raisin Counter","esmerelda@example.com","559-555-2397"
"Blain","Marilyn","Raisin Packager","marilyn@example.com","559-555-6565"
"Marks","Blair","VP Investor Relations","blair@example.com","559-555-6513"
"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"
>>> 
>>> # Differences:
>>> # 1. Carriage returns in one, but not the other
>>> # 2. Each field has quotes around it
>>> line
'"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"\r\n'
>>> 
>>> 
>>> print file.__doc__
file(name[, mode[, buffering]]) -> file object

Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files.
Add a '+' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.  The preferred way
to open a file is with the builtin open() function.
Add a 'U' to mode to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a '\n'
in Python.  Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
'\r', '\n', '\r\n' or a tuple containing all the newline types seen.

'U' cannot be combined with 'w' or '+' mode.

>>> ================================ RESTART ================================
>>> 
"Hettinger","Raymond","VP Raisin Smushing","raymond@example.com","559-555-1212"
"Thomas","Mary","Sr. Associate Raisin Design","mary@example.com","559-555-2300"
"Davis","Harold","Chief Raisin Picker","harold@example.com","559-555-2318"
"Masterson","Martin","Asst Raisin Smusher","martin@example.com","559-555-2348"
"Jones","David","Grape Ager","david@example.com","559-555-2379"
"Zapata","Luis","VP Grape Sales","luis@example.com","559-555-2301"
"Gunter","Fritz","Grape Smusher","fritz@example.com","559-555-2333"
"Pichon","Esmerela","Head Raisin Counter","esmerelda@example.com","559-555-2397"
"Blain","Marilyn","Raisin Packager","marilyn@example.com","559-555-6565"
"Marks","Blair","VP Investor Relations","blair@example.com","559-555-6513"
"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"
>>> line
'"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"\n'
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard_update.py", line 9, in <module>
    last, first, title, email, phone = data
ValueError: too many values to unpack
>>> data
['"Gump"', '"Forrest"', '"President', ' Ping Pong"', '"forrest@gump.com"', '"888-888-8888"']
>>> 
>>> f = open('notes/raisin_team_update.csv', 'rU')
>>> line = f.readline()
>>> line
'"Hettinger","Raymond","VP Raisin Smushing","raymond@example.com","559-555-1212"\n'
>>> data = line.strip().split(',')
>>> last, first, title, email, phone = data
>>> 
>>> last
'"Hettinger"'
>>> first
'"Raymond"'
>>> title
'"VP Raisin Smushing"'
>>> last.strip('"')
'Hettinger'
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/sharona/bossylobster-app-engine/learning-python/2015-12-07-workspace/vcard_update.py", line 9, in <module>
    last, first, title, email, phone = data
ValueError: too many values to unpack
>>> 
>>> data
['"Gump"', '"Forrest"', '"\\"President\\"', ' Ping Pong"', '"forrest@gump.com"', '"888-888-8888"']
>>> data[2]
'"\\"President\\"'
>>> line.strip()
'"Gump","Forrest","\\"President\\", Ping Pong","forrest@gump.com","888-888-8888"'
>>> title = """"\\"President\\", Ping Pong"""
>>> title
'"\\"President\\", Ping Pong'
>>> title = """"\\"President\\", Ping Pong""""
SyntaxError: EOL while scanning string literal
>>> title = """"\\"President\\", Ping Pong\""""
>>> title
'"\\"President\\", Ping Pong"'
>>> title.strip('"')
'\\"President\\", Ping Pong'
>>> 
>>> 
>>> 
>>> # re: Use brainpower
>>> # Dan says: use social momentum
>>> import csv
>>> help(csv)
Help on module csv:

NAME
    csv - CSV parsing and writing.

FILE
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py

MODULE DOCS
    http://docs.python.org/library/csv

DESCRIPTION
    This module provides classes that assist in the reading and writing
    of Comma Separated Value (CSV) files, and implements the interface
    described by PEP 305.  Although many CSV files are simple to parse,
    the format is not formally defined by a stable specification and
    is subtle enough that parsing lines of a CSV file with something
    like line.split(",") is bound to fail.  The module supports three
    basic APIs: reading, writing, and registration of dialects.
    
    
    DIALECT REGISTRATION:
    
    Readers and writers support a dialect argument, which is a convenient
    handle on a group of settings.  When the dialect argument is a string,
    it identifies one of the dialects previously registered with the module.
    If it is a class or instance, the attributes of the argument are used as
    the settings for the reader or writer:
    
        class excel:
            delimiter = ','
            quotechar = '"'
            escapechar = None
            doublequote = True
            skipinitialspace = False
            lineterminator = '\r\n'
            quoting = QUOTE_MINIMAL
    
    SETTINGS:
    
        * quotechar - specifies a one-character string to use as the 
            quoting character.  It defaults to '"'.
        * delimiter - specifies a one-character string to use as the 
            field separator.  It defaults to ','.
        * skipinitialspace - specifies how to interpret whitespace which
            immediately follows a delimiter.  It defaults to False, which
            means that whitespace immediately following a delimiter is part
            of the following field.
        * lineterminator -  specifies the character sequence which should 
            terminate rows.
        * quoting - controls when quotes should be generated by the writer.
            It can take on any of the following module constants:
    
            csv.QUOTE_MINIMAL means only when required, for example, when a
                field contains either the quotechar or the delimiter
            csv.QUOTE_ALL means that quotes are always placed around fields.
            csv.QUOTE_NONNUMERIC means that quotes are always placed around
                fields which do not parse as integers or floating point
                numbers.
            csv.QUOTE_NONE means that quotes are never placed around fields.
        * escapechar - specifies a one-character string used to escape 
            the delimiter when quoting is set to QUOTE_NONE.
        * doublequote - controls the handling of quotes inside fields.  When
            True, two consecutive quotes are interpreted as one during read,
            and when writing, each quote character embedded in the data is
            written as two quotes

CLASSES
    Dialect
        excel
            excel_tab
    DictReader
    DictWriter
    Sniffer
    exceptions.Exception(exceptions.BaseException)
        _csv.Error
    
    class Dialect
     |  Describe an Excel dialect.
     |  
     |  This must be subclassed (see csv.excel).  Valid attributes are:
     |  delimiter, quotechar, escapechar, doublequote, skipinitialspace,
     |  lineterminator, quoting.
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  delimiter = None
     |  
     |  doublequote = None
     |  
     |  escapechar = None
     |  
     |  lineterminator = None
     |  
     |  quotechar = None
     |  
     |  quoting = None
     |  
     |  skipinitialspace = None
    
    class DictReader
     |  Methods defined here:
     |  
     |  __init__(self, f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
     |  
     |  __iter__(self)
     |  
     |  next(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fieldnames
    
    class DictWriter
     |  Methods defined here:
     |  
     |  __init__(self, f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
     |  
     |  writeheader(self)
     |  
     |  writerow(self, rowdict)
     |  
     |  writerows(self, rowdicts)
    
    class Error(exceptions.Exception)
     |  Method resolution order:
     |      Error
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message
    
    class Sniffer
     |  "Sniffs" the format of a CSV file (i.e. delimiter, quotechar)
     |  Returns a Dialect object.
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  has_header(self, sample)
     |  
     |  sniff(self, sample, delimiters=None)
     |      Returns a dialect (or None) corresponding to the sample
    
    class excel(Dialect)
     |  Describe the usual properties of Excel-generated CSV files.
     |  
     |  Data and other attributes defined here:
     |  
     |  delimiter = ','
     |  
     |  doublequote = True
     |  
     |  lineterminator = '\r\n'
     |  
     |  quotechar = '"'
     |  
     |  quoting = 0
     |  
     |  skipinitialspace = False
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Dialect:
     |  
     |  __init__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Dialect:
     |  
     |  escapechar = None
    
    class excel_tab(excel)
     |  Describe the usual properties of Excel-generated TAB-delimited files.
     |  
     |  Method resolution order:
     |      excel_tab
     |      excel
     |      Dialect
     |  
     |  Data and other attributes defined here:
     |  
     |  delimiter = '\t'
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from excel:
     |  
     |  doublequote = True
     |  
     |  lineterminator = '\r\n'
     |  
     |  quotechar = '"'
     |  
     |  quoting = 0
     |  
     |  skipinitialspace = False
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Dialect:
     |  
     |  __init__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Dialect:
     |  
     |  escapechar = None

FUNCTIONS
    field_size_limit(...)
        Sets an upper limit on parsed fields.
            csv.field_size_limit([limit])
        
        Returns old limit. If limit is not given, no new limit is set and
        the old limit is returned
    
    get_dialect(...)
        Return the dialect instance associated with name.
        dialect = csv.get_dialect(name)
    
    list_dialects(...)
        Return a list of all know dialect names.
        names = csv.list_dialects()
    
    reader(...)
        csv_reader = reader(iterable [, dialect='excel']
                                [optional keyword args])
            for row in csv_reader:
                process(row)
        
        The "iterable" argument can be any object that returns a line
        of input for each iteration, such as a file object or a list.  The
        optional "dialect" parameter is discussed below.  The function
        also accepts optional keyword arguments which override settings
        provided by the dialect.
        
        The returned object is an iterator.  Each iteration returns a row
        of the CSV file (which can span multiple input lines):
    
    register_dialect(...)
        Create a mapping from a string name to a dialect class.
        dialect = csv.register_dialect(name, dialect)
    
    unregister_dialect(...)
        Delete the name/dialect mapping associated with a string name.
        csv.unregister_dialect(name)
    
    writer(...)
        csv_writer = csv.writer(fileobj [, dialect='excel']
                                    [optional keyword args])
            for row in sequence:
                csv_writer.writerow(row)
        
            [or]
        
            csv_writer = csv.writer(fileobj [, dialect='excel']
                                    [optional keyword args])
            csv_writer.writerows(rows)
        
        The "fileobj" argument can be any object that supports the file API.

DATA
    QUOTE_ALL = 1
    QUOTE_MINIMAL = 0
    QUOTE_NONE = 3
    QUOTE_NONNUMERIC = 2
    __all__ = ['QUOTE_MINIMAL', 'QUOTE_ALL', 'QUOTE_NONNUMERIC'
# IndentationError: ('unindent does not match any outer indentation level', ('<tokenize>', 1719, 4, "    __version__ = '1.0'\n"))
 'QUOTE_NO...
    __version__ = '1.0'

VERSION
    1.0


>>> ================================ RESTART ================================
>>> 
>>> 
>>> reader
<_csv.reader object at 0x10fc69280>
>>> f
<closed file 'notes/raisin_team_update.csv', mode 'rb' at 0x10fc6c030>
>>> ================================ RESTART ================================
>>> 
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
['Thomas', 'Mary', 'Sr. Associate Raisin Design', 'mary@example.com', '559-555-2300']
['Davis', 'Harold', 'Chief Raisin Picker', 'harold@example.com', '559-555-2318']
['Masterson', 'Martin', 'Asst Raisin Smusher', 'martin@example.com', '559-555-2348']
['Jones', 'David', 'Grape Ager', 'david@example.com', '559-555-2379']
['Zapata', 'Luis', 'VP Grape Sales', 'luis@example.com', '559-555-2301']
['Gunter', 'Fritz', 'Grape Smusher', 'fritz@example.com', '559-555-2333']
['Pichon', 'Esmerela', 'Head Raisin Counter', 'esmerelda@example.com', '559-555-2397']
['Blain', 'Marilyn', 'Raisin Packager', 'marilyn@example.com', '559-555-6565']
['Marks', 'Blair', 'VP Investor Relations', 'blair@example.com', '559-555-6513']
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
['Gump', 'Forrest', '\\President\\"', ' Ping Pong"', 'forrest@gump.com', '888-888-8888']
>>> 
>>> row
['Gump', 'Forrest', '\\President\\"', ' Ping Pong"', 'forrest@gump.com', '888-888-8888']
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> # 5:05pm, open turtle.py
>>> 
>>> from turtle import *
>>> import antigravity
>>> ================================ RESTART ================================
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> from turtle import *
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> 
>>> 
>>> 
>>> 
>>> from turtle import *
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> 
>>> from turtle import *
>>> dir()
['Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'Terminator', 'Turtle', 'TurtleScreen', 'Vec2D', '__builtins__', '__doc__', '__name__', '__package__', 'acos', 'addshape', 'asin', 'atan', 'atan2', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'ceil', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'cos', 'cosh', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'e', 'end_fill', 'end_poly', 'exitonclick', 'exp', 'fabs', 'fd', 'fill', 'fillcolor', 'floor', 'fmod', 'forward', 'frexp', 'get_poly', 'getcanvas', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'hypot', 'isdown', 'isvisible', 'ldexp', 'left', 'listen', 'log', 'log10', 'lt', 'mainloop', 'mode', 'modf', 'onclick', 'ondrag', 'onkey', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pi', 'pos', 'position', 'pow', 'pu', 'radians', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'showturtle', 'sin', 'sinh', 'speed', 'sqrt', 'st', 'stamp', 'tan', 'tanh', 'tilt', 'tiltangle', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
>>> 
>>> 
>>> import turtle
>>> dir(turtle)
['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__', '__builtins__', '__doc__', '__file__', '__forwardmethods', '__func_body', '__methodDict', '__methods', '__name__', '__package__', '__stringBody', '_alias_list', '_make_global_funcs', '_math_functions', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'acos', 'acosh', 'addshape', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'ceil', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'copysign', 'cos', 'cosh', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'e', 'end_fill', 'end_poly', 'erf', 'erfc', 'exitonclick', 'exp', 'expm1', 'fabs', 'factorial', 'fd', 'fill', 'fillcolor', 'floor', 'fmod', 'forward', 'frexp', 'fsum', 'gamma', 'get_poly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'hypot', 'isdown', 'isfile', 'isinf', 'isnan', 'isvisible', 'join', 'ldexp', 'left', 'lgamma', 'listen', 'log', 'log10', 'log1p', 'lt', 'mainloop', 'math', 'mode', 'modf', 'onclick', 'ondrag', 'onkey', 'onrelease', 'onscreenclick', 'ontimer', 'os', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pi', 'pos', 'position', 'pow', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'showturtle', 'sin', 'sinh', 'speed', 'split', 'sqrt', 'st', 'stamp', 'tan', 'tanh', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'trunc', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
>>> dir()
['Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'Terminator', 'Turtle', 'TurtleScreen', 'Vec2D', '__builtins__', '__doc__', '__name__', '__package__', 'acos', 'addshape', 'asin', 'atan', 'atan2', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'ceil', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'cos', 'cosh', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'e', 'end_fill', 'end_poly', 'exitonclick', 'exp', 'fabs', 'fd', 'fill', 'fillcolor', 'floor', 'fmod', 'forward', 'frexp', 'get_poly', 'getcanvas', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'hypot', 'isdown', 'isvisible', 'ldexp', 'left', 'listen', 'log', 'log10', 'lt', 'mainloop', 'mode', 'modf', 'onclick', 'ondrag', 'onkey', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pi', 'pos', 'position', 'pow', 'pu', 'radians', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'showturtle', 'sin', 'sinh', 'speed', 'sqrt', 'st', 'stamp', 'tan', 'tanh', 'tilt', 'tiltangle', 'title', 'towards', 'tracer', 'turtle', 'turtles', 'turtlesize', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']
>>> 
>>> 
>>> 
>>> clearscreen()
>>> 
>>> 
>>> 
>>> forward(100)
>>> right(90)
>>> 
>>> def turn_right():
	forward(100)
	right(90)

	
>>> turn_right
<function turn_right at 0x10cf82668>
>>> 
>>> turn_right()
>>> turn_right()
turn_right()
>>> 
>>> turn_right()
>>> turn_right()
>>> turn_right()
turn_right()
>>> 
>>> turn_right()
>>> 
>>> 
>>> clearscreen()
>>> 
>>> def make_box():
	turn_right()
	turn_right()
	turn_right()
	turn_right()

	
>>> make_box()
>>> 
>>> clearscreen()
>>> 
>>> def make_box():
	for i in range(4):
		turn_right()

		
>>> s = 'abcdefg'
>>> s[:4]
'abcd'
>>> range(4)
[0, 1, 2, 3]
>>> s[2:3]
'c'
>>> s
'abcdefg'
>>> s[2]
'c'
>>> range(2, 3)
[2]
>>> range(0, 8, 2)
[0, 2, 4, 6]
>>> make_box()
>>> def make_box():
	for _ in range(4):
		turn_right()

		
>>> clearscreen()
>>> 
>>> make_box()
>>> 
>>> 
>>> make_box()
>>> right(30)
>>> make_box()
>>> 
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> right(30)
>>> make_box()
>>> clearscreen()
>>> 
>>> 
>>> for _ in range(12):
	make_box()
	right(30)

>>> 
>>> def star(n):
	angle = 360 / n
	for _ in range(n):
		make_box()
		right(angle)

		
>>> 
>>> clearscreen()
>>> 
>>> # star(7)
>>> n = 7
>>> angle = 360 / n
>>> angle
51
>>> angle
51
>>> 
>>> 360 // n
51
>>> 360.0 / n
51.42857142857143
>>> 
>>> from __future__ import division
>>> 
>>> 360 / n
51.42857142857143
>>> 
>>> def star(n):
	angle = 360 // n
	for _ in range(n):
		make_box()
		right(angle)

		
>>> 
>>> star(7)
>>> 
>>> 
>>> clearscreen()
>>> 
>>> star(6)
>>> begin_fill()
>>> color('red')
>>> fill_color('purple')

Traceback (most recent call last):
  File "<pyshell#1466>", line 1, in <module>
    fill_color('purple')
NameError: name 'fill_color' is not defined
>>> fillcolor('purple')
>>> star(6)
>>> 
>>> end_fill()
>>> clearscreen()
>>> bye()
>>> 