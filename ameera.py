Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_data= {
	'name': 'Ameera',
	'age': 20,
	'university': 'COMSATS Lahore campus',
	}
>>> for my data in my_data.items():
	
SyntaxError: invalid syntax
>>> for key, value in my_data.items():
	print(f"{key}": "{value}")
	
SyntaxError: invalid syntax
>>> for key,value in my_data.items():
	print(f'key:{key}')
	
SyntaxError: invalid syntax
>>>  for key,value in my_data.items():
	 
SyntaxError: unexpected indent
>>> for key,value in my_data.items():
	print(f"Key: {key}"}
	
SyntaxError: invalid syntax
>>> for key,value in my_data.items():
	print(my_data.keys())

	
dict_keys(['age', 'name', 'university'])
dict_keys(['age', 'name', 'university'])
dict_keys(['age', 'name', 'university'])
>>> for key,value in my_data.items():
	print(my_data.items())

	
dict_items([('age', 20), ('name', 'Ameera'), ('university', 'COMSATS Lahore campus')])
dict_items([('age', 20), ('name', 'Ameera'), ('university', 'COMSATS Lahore campus')])
dict_items([('age', 20), ('name', 'Ameera'), ('university', 'COMSATS Lahore campus')])
>>> 
