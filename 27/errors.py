2/0
# ZeroDivisionError: division by zero

print(Ahoj)
# NameError: name 'Ahoj' is not defined

int('String')
# ValueError: invalid literal for int() with base 10: 'String'

len(9)
# TypeError: object of type 'int' has no len()

'abc'.len
# AttributeError: 'str' object has no attribute 'len'

import neexistujiciKnihovna
# ModuleNotFoundError: No module named 'neexistujiciKnihovna'

pole = [1, 2, 3]
pole[10]
# IndexError: list index out of range

for i in range(5):
print(i)
# SyntaxError: expected an indented block after 'for' statement on line 1
