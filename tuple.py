Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Ameera Attique
>>> #SP24-BBA-009
>>> Ms_A_REGISTRATION=('SP24-BBA-009.,)
		   
SyntaxError: EOL while scanning string literal
>>> ms_a_registration=('sp24-bba-009',)
>>> #a mised tuple
>>> mixed_tuple=('apple',3.14, 1, true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mixed_tuple=('apple',3.14, 1, true)
NameError: name 'true' is not defined
>>> mixed_tuple=('apple',1,3.14,'true')
>>> #a single item tuple
>>> single_item_tuple=(5,)
>>> candy=('cola','orange','apple')
>>> print(andy_tuple(0))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(andy_tuple(0))
NameError: name 'andy_tuple' is not defined
>>> print(candy_tuple(0))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(candy_tuple(0))
NameError: name 'candy_tuple' is not defined
>>> print(candy_tuple[0])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(candy_tuple[0])
NameError: name 'candy_tuple' is not defined
>>> fruits=('appple','mango')
>>> print(fruits_tuple[0])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(fruits_tuple[0])
NameError: name 'fruits_tuple' is not defined
>>> candy_tuple=('cola','orange')
>>> print(candy_tuple(0))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(candy_tuple(0))
TypeError: 'tuple' object is not callable
>>> candy_tuple=('apple','mango')
>>> candy_tuple(0)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    candy_tuple(0)
TypeError: 'tuple' object is not callable
>>> candy_tuple[0]=
SyntaxError: invalid syntax
>>> print(candy_tuple[0])
apple
>>> #modifying
>>> candy_('apple','cola')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    candy_('apple','cola')
NameError: name 'candy_' is not defined
>>> candy_tuple=('cola','apple')
>>> candy_tuple[0]='blueberry'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    candy_tuple[0]='blueberry'
TypeError: 'tuple' object does not support item assignment
>>> tuple1=(67,45,89)
>>> tuple2=(34,78,88)
>>> combined_tuple= tuple1 + tuple2
>>> print(combined_tuple)
(67, 45, 89, 34, 78, 88)
>>> tuple1=('hello',)
>>> repeated_tuple= tuple1*3
>>> print(repeated_tuple)
('hello', 'hello', 'hello')
>>> candy_tuple=('apple','cola','apple','orange')
>>> print(candy_tuple.count('appl'))
0
>>> print(candy_tuple.count('apple'))
2
>>> #tuple slicing
>>> numbers= (0,1,2,3,4,5,6)
>>> print(numbers[1:4[)
	      
SyntaxError: invalid syntax
>>> print(numbers[1:4])
(1, 2, 3)
>>> candy_tuple=('apple','cola')
>>> print(candy.index('apple'))
2
>>> 
