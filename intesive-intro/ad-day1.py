Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> print "Hi"
Hi
>>> pwd

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> ================================ RESTART ================================
>>> 
====== Source: http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt ======
                      Starting download at Mon Dec  7 10:56:45 2015                       
http://bossylobster.appspot.com/learning-python/2015-12-07/links.txt
200  OK           http://www.bossylobster.com/learning-python/shared/raisin_team.csv
                  --> notes/raisin_team.csv     (updated) 
200  OK           http://www.bossylobster.com/learning-python/shared/PythonAwesome.pdf
                  --> notes/PythonAwesome.pdf   (updated) 
>>> import os
>>> os.getcwd()
'/Users/aradhana/Work/Learn/courses/python/intro'
>>> dir()
['Pool', 'Response', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cStringIO', 'class_name', 'dirname', 'download', 'dumbdbm', 'etags', 'gzip', 'line', 'links_text', 'links_url', 'mapper', 'namedtuple', 'os', 'pprint', 're', 'sys', 'targets', 'threading', 'time', 'url_template', 'urllib2', 'urlretrieve', 'writefile']
>>> pprint dir()
SyntaxError: invalid syntax
>>> 
>>> tmp = "tmp"
>>> dir
<built-in function dir>
>>> dir()
['Pool', 'Response', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cStringIO', 'class_name', 'dirname', 'download', 'dumbdbm', 'etags', 'gzip', 'line', 'links_text', 'links_url', 'mapper', 'namedtuple', 'os', 'pprint', 're', 'sys', 'targets', 'threading', 'time', 'tmp', 'url_template', 'urllib2', 'urlretrieve', 'writefile']
>>> tmp
'tmp'
>>> pprint tmp
SyntaxError: invalid syntax
>>> print tmp
tmp
>>> pprint(tmp)
'tmp'
>>> del tmp
>>> print tmp

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print tmp
NameError: name 'tmp' is not defined
>>> 'this is a tab \t that was a tab'
'this is a tab \t that was a tab'
>>> print 'this is a tab \t that was a tab'
this is a tab 	 that was a tab
>>> r'this is a tab \t that was a tab'
'this is a tab \\t that was a tab'
>>> b'abc'
'abc'
>>> # b - bytestring
>>> # r - raw
>>> # u - unicode
>>> u'abc'
u'abc'
>>> type("abc")
<type 'str'>
>>> type(u"abc")
<type 'unicode'>
>>> type(b"abc")
<type 'str'>
>>> class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print "Hi, I'm a dog and my name is ", self.name

		
>>> d = Dog("Johnny")
>>> d.bark
<bound method Dog.bark of <__main__.Dog instance at 0x107c538c0>>
>>> d.bark()
Hi, I'm a dog and my name is  Johnny
>>> 
>>> d.__class__
<class __main__.Dog at 0x1082882c0>
>>> dir(d)
['__doc__', '__init__', '__module__', 'bark', 'name']
>>> c = Dog()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c = Dog()
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> # not passing an argument gives a clear error: init() takes 2 args and we are not passing the name
>>> s = [1, 2, 3]
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

>>> s = "restart"
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print s
restart
>>> for attr in dir(s):
	print attr

	
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
>>> for attr in dir(s):
	print s.attr()

	

Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    print s.attr()
AttributeError: 'str' object has no attribute 'attr'
>>> print s.upper()
RESTART
>>> for attr in dirs():
	print s.attr

	

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for attr in dirs():
NameError: name 'dirs' is not defined
>>> for attr in dir(s):
	print s.attr

	

Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print s.attr
AttributeError: 'str' object has no attribute 'attr'
>>> print s
restart
>>> help s.title()
SyntaxError: invalid syntax
>>> help (s.title())
no Python documentation found for 'Restart'

>>> help(title)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    help(title)
NameError: name 'title' is not defined
>>> help(s.title)
Help on built-in function title:

title(...)
    S.title() -> string
    
    Return a titlecased version of S, i.e. words start with uppercase
    characters, all remaining cased characters have lowercase.

>>> print s.title()
Restart
>>> print s.upper.tilte()

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print s.upper.tilte()
AttributeError: 'builtin_function_or_method' object has no attribute 'tilte'
>>> print s.upper.title()

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print s.upper.title()
AttributeError: 'builtin_function_or_method' object has no attribute 'title'
>>> help(s.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> print s.center(5, '=')
restart
>>> print s.center(15, '=')
====restart====
>>> print s.center(25, '=')
=========restart=========
>>> print s.upper().center(25, '=')
=========RESTART=========
>>> space = [' ' , ' ']
>>> print s.join(space)
 restart 
>>> print s.join(space).upper()
 RESTART 
>>> print s.join(space).upper().center(12)
  RESTART   
>>> print s.join(space).upper().center(12, '=')
= RESTART ==
>>> print s.join(space).upper().center(72, '=')
=============================== RESTART ================================
>>> __contains__
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
>>> for attr in dir(s):
	print s.attr()



Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    print s.attr()
AttributeError: 'str' object has no attribute 'attr'
>>> print s.upper()
RESTART
>>> for attr in dirs():
	print s.attr



Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for attr in dirs():
NameError: name 'dirs' is not defined
>>> for attr in dir(s):
	print s.attr



Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print s.attr
AttributeError: 'str' object has no attribute 'attr'
>>> print s
restart
>>> help s.title()
SyntaxError: invalid syntax
>>> help (s.title())
no Python documentation found for 'Restart'

>>> help(title)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    help(title)
NameError: name 'title' is not defined
>>> help(s.title)
Help on built-in function title:

title(...)
    S.title() -> string

    Return a titlecased version of S, i.e. words start with uppercase
    characters, all remaining cased characters have lowercase.

>>> print s.title()
Restart
>>> print s.upper.tilte()

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print s.upper.tilte()
AttributeError: 'builtin_function_or_method' object has no attribute 'tilte'
>>> print s.upper.title()

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print s.upper.title()
AttributeError: 'builtin_function_or_method' object has no attribute 'title'
>>> help(s.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string

    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> print s.center(5, '=')
restart
>>> print s.center(15, '=')
====restart====
>>> print s.center(25, '=')
=========restart=========
>>> print s.upper().center(25, '=')
=========RESTART=========
>>> space = [' ' , ' ']
>>> print s.join(space)
 restart
>>> print s.join(space).upper()
 RESTART
>>> print s.join(space).upper().center(12)
  RESTART
>>> print s.join(space).upper().center(12, '=')
= RESTART ==
>>> print s.join(space).upper().center(72, '=')
=============================== RESTART ================================

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    __contains__
NameError: name '__contains__' is not defined
>>> __contains__
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
>>> for attr in dir(s):
	print s.attr()



Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    print s.attr()
AttributeError: 'str' object has no attribute 'attr'
>>> print s.upper()
RESTART
>>> for attr in dirs():
	print s.attr



Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for attr in dirs():
NameError: name 'dirs' is not defined
>>> for attr in dir(s):
	print s.attr



Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print s.attr
AttributeError: 'str' object has no attribute 'attr'
>>> print s
restart
>>> help s.title()
SyntaxError: invalid syntax
>>> help (s.title())
no Python documentation found for 'Restart'

>>> help(title)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    help(title)
NameError: name 'title' is not defined
>>> help(s.title)
Help on built-in function title:

title(...)
    S.title() -> string

    Return a titlecased version of S, i.e. words start with uppercase
    characters, all remaining cased characters have lowercase.

>>> print s.title()
Restart
>>> print s.upper.tilte()

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print s.upper.tilte()
AttributeError: 'builtin_function_or_method' object has no attribute 'tilte'
>>> print s.upper.title()

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print s.upper.title()
AttributeError: 'builtin_function_or_method' object has no attribute 'title'
>>> help(s.center)
Help on built-in function center:

center(...)
    S.center(width[, fillchar]) -> string

    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> print s.center(5, '=')
restart
>>> print s.center(15, '=')
====restart====
>>> print s.center(25, '=')
=========restart=========
>>> print s.upper().center(25, '=')
=========RESTART=========
>>> space = [' ' , ' ']
>>> print s.join(space)
 restart
>>> print s.join(space).upper()
 RESTART
>>> print s.join(space).upper().center(12)
  RESTART
>>> print s.join(space).upper().center(12, '=')
= RESTART ==
>>> print s.join(space).upper().center(72, '=')
=============================== RESTART ================================

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    __contains__
NameError: name '__contains__' is not defined
>>> print s.join(space).upper().center(72, '=')
=============================== RESTART ================================
>>> new_s = s.join(space).upper().center(72, '=')
>>> final = ' '.join(">>>", new_s)

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    final = ' '.join(">>>", new_s)
TypeError: join() takes exactly one argument (2 given)
>>> final = ' '.join([">>>", new_s])
>>> print final
>>> =============================== RESTART ================================
>>> s = 'a, b, c, d, e'
>>> print s.split()
['a,', 'b,', 'c,', 'd,', 'e']
>>> print s.split(',')
['a', ' b', ' c', ' d', ' e']
>>> # The above output includes spaces!
>>> print s.split(', ')
['a', 'b', 'c', 'd', 'e']
>>> s = "This string has many words."
>>> # Slicing can be used to create sub-strings.
>>> print s[:10]
This strin
>>> # Python supports -ve indexing. See below.
>>> print s[-1]
.
>>> print [-10"]
       
SyntaxError: EOL while scanning string literal
>>> print [-10]
[-10]
>>> print s[-10:]
any words.
>>> # Reversing a string or list is very easy. See below.
>>> str = "Reverse this string!"
>>> rev_list = [5, 4, 3, 2, 1]
>>> print str[::-1]
!gnirts siht esreveR
>>> print rev_list[::-1]
[1, 2, 3, 4, 5]
>>> int(ff, 2)

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    int(ff, 2)
NameError: name 'ff' is not defined
>>> 
>>> int('ff', 2)

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    int('ff', 2)
ValueError: invalid literal for int() with base 2: 'ff'
>>> 
>>> L = [1, 2, 3]
>>> T = (1, 2, 3) 	# tuple
>>> Lset = set(dir(L))	# set of dir(L)
>>> Tset = set(dir(T))	# set of dir(T)
>>> print (Lset - Tset)
set(['sort', 'insert', '__reversed__', '__delslice__', 'reverse', 'extend', '__delitem__', '__setslice__', 'remove', '__setitem__', '__iadd__', 'pop', 'append', '__imul__'])
>>> # i.e., list supports the above methods other than the what a tuple can do
>>> 
>>> 
>>> # Dicts
>>> d1 = {1: 3, 5: 10, 11: -6 }
>>> print d1
{1: 3, 11: -6, 5: 10}
>>> d2 = {1: 3, 5: 10, 11: -6}
>>> print d2
{1: 3, 11: -6, 5: 10}
>>> # Dicts order is dependent on the runtime hash function and may differ on different machines!
>>> print d1[5]
10
>>> print d1[10]

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print d1[10]
KeyError: 10
>>> print d1[11]
-6
>>> pprint dir(d1)
SyntaxError: invalid syntax
>>> pprint dir(d1)
SyntaxError: invalid syntax
>>> print dir(d1)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> print d1.values()
[3, -6, 10]
>>> print d1.has_key
<built-in method has_key of dict object at 0x10827c6e0>
>>> print d1.has_key(5)
True
>>> print d1.has_key(15)
False
>>> print d1
{1: 3, 11: -6, 5: 10}
>>> print d1.viewitems()
dict_items([(1, 3), (11, -6), (5, 10)])
>>> 1 < ' '
True
>>> 
>>> 
>>> 
>>> ninjas = {"Donatello": "Bo",}
>>> ninjas.clear()
>>> ninjas = {"Donatello": "Bo",}
>>> ninjas = {"Donatello": "Bo",}ninjas.clear()
SyntaxError: invalid syntax
>>> ninjas.clear()
>>> ninjas = {"Donatello": "Bo", "Michelanglo": "Nunchuk", "Rafael": "Sai", "Leonardo": "Katana"}
>>> for ninja, weapon in ninjas:
	print ninja, "--->" weapon
	
SyntaxError: invalid syntax
>>> for ninja, weapon in ninjas:
	print ninja, "--->", weapon

	

Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    for ninja, weapon in ninjas:
ValueError: too many values to unpack
>>> print ninjas
{'Michelanglo': 'Nunchuk', 'Donatello': 'Bo', 'Leonardo': 'Katana', 'Rafael': 'Sai'}
>>> for ninja, weapon in ninjas.items():
	print ninja, "--->", weapon

	
Michelanglo ---> Nunchuk
Donatello ---> Bo
Leonardo ---> Katana
Rafael ---> Sai
>>> for ninja, weapon in ninjas.items():
	print "%14s yields a %s" %(ninja, weapon)

	
   Michelanglo yields a Nunchuk
     Donatello yields a Bo
      Leonardo yields a Katana
        Rafael yields a Sai
>>> ================================ RESTART ================================
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> ================================ RESTART ================================
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__']
>>> print __doc__

Script for making vCards.

Making vCars (with QR code) for brother-in-law.

>>> ================================ RESTART ================================
>>> 
>>> print __doc__

File: vcard.py
Desc: Script for making vCards.
	  Making vCars (with QR code) for brother-in-law.

>>> ================================ RESTART ================================
>>> 
>>> print __doc__
None
>>> ================================ RESTART ================================
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'file_hdl', 'filename']
>>> __doc__
'\nFile: vcard.py\n\nDesc: \nScript for making vCards.\nMaking vCars (with QR code) for brother-in-law.\n\n'
>>> print __doc__

File: vcard.py

Desc: 
Script for making vCards.
Making vCars (with QR code) for brother-in-law.


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
>>> help(line.strip())

Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    help(line.strip())
NameError: name 'line' is not defined
>>> help(line.strip)

Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    help(line.strip)
NameError: name 'line' is not defined
>>> print line

Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    print line
NameError: name 'line' is not defined
>>> print each_line
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> help(each_line.strip())
no Python documentation found for 'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'

>>> help(each_line.strip)
Help on built-in function strip:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> help(file_hdl.close)
Help on built-in function close:

close(...)
    close() -> None or (perhaps) an integer.  Close the file.
    
    Sets data attribute .closed to True.  A closed file cannot be used for
    further I/O operations.  close() may be called more than once without
    error.  Some kinds of file objects (for example, opened by popen())
    may return an exit status upon closing.

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
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 11, in <module>
    file_hdl = open(filename)
IOError: [Errno 2] No such file or directory: 'notes/aisin_team.csv'
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 11, in <module>
    file_hdl = open(filename)
IOError: [Errno 2] No such file or directory: 'notes/aisin_team.csv'
>>> ================================ RESTART ================================
>>> 
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 21, in <module>
    file_hdl.close()
NameError: name 'file_hdl' is not defined
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
>>> ================================ RESTART ================================
>>> 
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 22, in <module>
    file_hdl.close()
NameError: name 'file_hdl' is not defined
>>> ================================ RESTART ================================
>>> 
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 14, in <module>
    file_hdl = open(filename)
IOError: [Errno 2] No such file or directory: 'notes/aisin_team.csv'
>>> ================================ RESTART ================================
>>> 
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 22, in <module>
    file_hdl.close()
NameError: name 'file_hdl' is not defined
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 24, in <module>
    (first_name, last_name, title, email, phone_number)
TypeError: not all arguments converted during string formatting
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 25, in <module>
    (first_name, last_name, title, email, phone_number)
TypeError: not all arguments converted during string formatting
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
ERROR!

Traceback (most recent call last):
  File "/Users/aradhana/Work/Learn/courses/python/intro/vcard.py", line 24, in <module>
    print "% %s, %s, %s, %s" % (first_name, last_name, title, email, phone_number)
TypeError: not all arguments converted during string formatting
>>> ================================ RESTART ================================
>>> 
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
Raymond Hettinger, VP Raisin Smushing, raymond@example.com, 559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
['Thomas', 'Mary', 'Sr. Associate Raisin Design', 'mary@example.com', '559-555-2300']
Mary Thomas, Sr. Associate Raisin Design, mary@example.com, 559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
['Davis', 'Harold', 'Chief Raisin Picker', 'harold@example.com', '559-555-2318']
Harold Davis, Chief Raisin Picker, harold@example.com, 559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
['Masterson', 'Martin', 'Asst Raisin Smusher', 'martin@example.com', '559-555-2348']
Martin Masterson, Asst Raisin Smusher, martin@example.com, 559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
['Jones', 'David', 'Grape Ager', 'david@example.com', '559-555-2379']
David Jones, Grape Ager, david@example.com, 559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
['Zapata', 'Luis', 'VP Grape Sales', 'luis@example.com', '559-555-2301']
Luis Zapata, VP Grape Sales, luis@example.com, 559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2333
['Gunter', 'Fritz', 'Grape Smusher', 'fritz@example.com', '559-555-2333']
Fritz Gunter, Grape Smusher, fritz@example.com, 559-555-2333
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
['Pichon', 'Esmerela', 'Head Raisin Counter', 'esmerelda@example.com', '559-555-2397']
Esmerela Pichon, Head Raisin Counter, esmerelda@example.com, 559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-6565
['Blain', 'Marilyn', 'Raisin Packager', 'marilyn@example.com', '559-555-6565']
Marilyn Blain, Raisin Packager, marilyn@example.com, 559-555-6565
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
['Marks', 'Blair', 'VP Investor Relations', 'blair@example.com', '559-555-6513']
Blair Marks, VP Investor Relations, blair@example.com, 559-555-6513
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
Gertrude Schmidt, VP Business Development, gertrude@example.com, 559-555-6700
ERROR!
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger, VP Raisin Smushing, raymond@example.com, 559-555-1212
Mary Thomas, Sr. Associate Raisin Design, mary@example.com, 559-555-2300
Harold Davis, Chief Raisin Picker, harold@example.com, 559-555-2318
Martin Masterson, Asst Raisin Smusher, martin@example.com, 559-555-2348
David Jones, Grape Ager, david@example.com, 559-555-2379
Luis Zapata, VP Grape Sales, luis@example.com, 559-555-2301
Fritz Gunter, Grape Smusher, fritz@example.com, 559-555-2333
Esmerela Pichon, Head Raisin Counter, esmerelda@example.com, 559-555-2397
Marilyn Blain, Raisin Packager, marilyn@example.com, 559-555-6565
Blair Marks, VP Investor Relations, blair@example.com, 559-555-6513
Gertrude Schmidt, VP Business Development, gertrude@example.com, 559-555-6700
ERROR!
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger, VP Raisin Smushing, raymond@example.com, 559-555-1212
Mary Thomas, Sr. Associate Raisin Design, mary@example.com, 559-555-2300
Harold Davis, Chief Raisin Picker, harold@example.com, 559-555-2318
Martin Masterson, Asst Raisin Smusher, martin@example.com, 559-555-2348
David Jones, Grape Ager, david@example.com, 559-555-2379
Luis Zapata, VP Grape Sales, luis@example.com, 559-555-2301
Fritz Gunter, Grape Smusher, fritz@example.com, 559-555-2333
Esmerela Pichon, Head Raisin Counter, esmerelda@example.com, 559-555-2397
Marilyn Blain, Raisin Packager, marilyn@example.com, 559-555-6565
Blair Marks, VP Investor Relations, blair@example.com, 559-555-6513
Gertrude Schmidt, VP Business Development, gertrude@example.com, 559-555-6700
ERROR!
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger, VP Raisin Smushing, raymond@example.com, 559-555-1212
Mary Thomas, Sr. Associate Raisin Design, mary@example.com, 559-555-2300
Harold Davis, Chief Raisin Picker, harold@example.com, 559-555-2318
Martin Masterson, Asst Raisin Smusher, martin@example.com, 559-555-2348
David Jones, Grape Ager, david@example.com, 559-555-2379
Luis Zapata, VP Grape Sales, luis@example.com, 559-555-2301
Fritz Gunter, Grape Smusher, fritz@example.com, 559-555-2333
Esmerela Pichon, Head Raisin Counter, esmerelda@example.com, 559-555-2397
Marilyn Blain, Raisin Packager, marilyn@example.com, 559-555-6565
Blair Marks, VP Investor Relations, blair@example.com, 559-555-6513
Gertrude Schmidt, VP Business Development, gertrude@example.com, 559-555-6700
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger | VP Raisin Smushing | raymond@example.com | 559-555-1212
Mary Thomas | Sr. Associate Raisin Design | mary@example.com | 559-555-2300
Harold Davis | Chief Raisin Picker | harold@example.com | 559-555-2318
Martin Masterson | Asst Raisin Smusher | martin@example.com | 559-555-2348
David Jones | Grape Ager | david@example.com | 559-555-2379
Luis Zapata | VP Grape Sales | luis@example.com | 559-555-2301
Fritz Gunter | Grape Smusher | fritz@example.com | 559-555-2333
Esmerela Pichon | Head Raisin Counter | esmerelda@example.com | 559-555-2397
Marilyn Blain | Raisin Packager | marilyn@example.com | 559-555-6565
Blair Marks | VP Investor Relations | blair@example.com | 559-555-6513
Gertrude Schmidt | VP Business Development | gertrude@example.com | 559-555-6700
>>> ================================ RESTART ================================
>>> 
Error!
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger | VP Raisin Smushing | raymond@example.com | 559-555-1212
Mary Thomas | Sr. Associate Raisin Design | mary@example.com | 559-555-2300
Harold Davis | Chief Raisin Picker | harold@example.com | 559-555-2318
Martin Masterson | Asst Raisin Smusher | martin@example.com | 559-555-2348
David Jones | Grape Ager | david@example.com | 559-555-2379
Luis Zapata | VP Grape Sales | luis@example.com | 559-555-2301
Fritz Gunter | Grape Smusher | fritz@example.com | 559-555-2333
Esmerela Pichon | Head Raisin Counter | esmerelda@example.com | 559-555-2397
Marilyn Blain | Raisin Packager | marilyn@example.com | 559-555-6565
Blair Marks | VP Investor Relations | blair@example.com | 559-555-6513
Gertrude Schmidt | VP Business Development | gertrude@example.com | 559-555-6700
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger | VP Raisin Smushing | raymond@example.com | 559-555-1212
Mary Thomas | Sr. Associate Raisin Design | mary@example.com | 559-555-2300
Harold Davis | Chief Raisin Picker | harold@example.com | 559-555-2318
Martin Masterson | Asst Raisin Smusher | martin@example.com | 559-555-2348
David Jones | Grape Ager | david@example.com | 559-555-2379
Luis Zapata | VP Grape Sales | luis@example.com | 559-555-2301
Fritz Gunter | Grape Smusher | fritz@example.com | 559-555-2333
Esmerela Pichon | Head Raisin Counter | esmerelda@example.com | 559-555-2397
Marilyn Blain | Raisin Packager | marilyn@example.com | 559-555-6565
Blair Marks | VP Investor Relations | blair@example.com | 559-555-6513
Gertrude Schmidt | VP Business Development | gertrude@example.com | 559-555-6700
>>> ================================ RESTART ================================
>>> 
need more than 3 values to unpack
>>> ================================ RESTART ================================
>>> 
need more than 3 values to unpack
>>> ================================ RESTART ================================
>>> 
Raymond Hettinger | VP Raisin Smushing | raymond@example.com | 559-555-1212
Mary Thomas | Sr. Associate Raisin Design | mary@example.com | 559-555-2300
Harold Davis | Chief Raisin Picker | harold@example.com | 559-555-2318
Martin Masterson | Asst Raisin Smusher | martin@example.com | 559-555-2348
David Jones | Grape Ager | david@example.com | 559-555-2379
Luis Zapata | VP Grape Sales | luis@example.com | 559-555-2301
Fritz Gunter | Grape Smusher | fritz@example.com | 559-555-2333
Esmerela Pichon | Head Raisin Counter | esmerelda@example.com | 559-555-2397
Marilyn Blain | Raisin Packager | marilyn@example.com | 559-555-6565
Blair Marks | VP Investor Relations | blair@example.com | 559-555-6513
Gertrude Schmidt | VP Business Development | gertrude@example.com | 559-555-6700
>>> ================================ RESTART ================================
>>> 
join() takes exactly one argument (2 given)
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Raymond-Hettinger.vcf
Mary-Thomas.vcf
Harold-Davis.vcf
Martin-Masterson.vcf
David-Jones.vcf
Luis-Zapata.vcf
Fritz-Gunter.vcf
Esmerela-Pichon.vcf
Marilyn-Blain.vcf
Blair-Marks.vcf
Gertrude-Schmidt.vcf
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond-Hettinger.vcf to disk.
Just wrote Mary-Thomas.vcf to disk.
Just wrote Harold-Davis.vcf to disk.
Just wrote Martin-Masterson.vcf to disk.
Just wrote David-Jones.vcf to disk.
Just wrote Luis-Zapata.vcf to disk.
Just wrote Fritz-Gunter.vcf to disk.
Just wrote Esmerela-Pichon.vcf to disk.
Just wrote Marilyn-Blain.vcf to disk.
Just wrote Blair-Marks.vcf to disk.
Just wrote Gertrude-Schmidt.vcf to disk.
>>> Just wrote Marilyn-Blain.vcf to disk.
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> URL = "http://api.qrserver.com/v1/create-qr-code/?data=HelloWorld!&size=100x100"
>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_asciire', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', '_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'always_safe', 'base64', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'noheaders', 'os', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 'quote_plus', 're', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test1', 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']
>>> # Make a connection
>>> cnxn = urllib.urlopen(URL)
data 
>>> data = cnxn.read()
>>> cnxn.close()
>>> print data
ﾉPNG



>>> 
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> dprrr

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    dprrr
NameError: name 'dprrr' is not defined
>>> 
>>> len(data)
281
>>> with oepn("hello-world.png", 'w') as png_file:
	png_file.write(data)

	

Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    with oepn("hello-world.png", 'w') as png_file:
NameError: name 'oepn' is not defined
>>> 
>>> 
>>> 
>>> 
>>> with oepn("hello-world.png", 'w') as png_file:
	png_file.write(data)

	

Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    with oepn("hello-world.png", 'w') as png_file:
NameError: name 'oepn' is not defined
>>> with oppe
("hello-world.png", 'w') as png_file:
	png_file.write(data)

	
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond-Hettinger.vcf to disk.
name 'urllib' is not defined
>>> ================================ RESTART ================================
>>> 
Just wrote Raymond-Hettinger.vcf to disk.
Just wrote Mary-Thomas.vcf to disk.
Just wrote Harold-Davis.vcf to disk.
Just wrote Martin-Masterson.vcf to disk.
Just wrote David-Jones.vcf to disk.
Just wrote Luis-Zapata.vcf to disk.
Just wrote Fritz-Gunter.vcf to disk.
Just wrote Esmerela-Pichon.vcf to disk.
Just wrote Marilyn-Blain.vcf to disk.
Just wrote Blair-Marks.vcf to disk.
Just wrote Gertrude-Schmidt.vcf to disk.
>>> 