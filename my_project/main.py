'''
---------- 1st way to import the module ----------

import my_calculator.addition
import my_calculator.substraction

result_1 = my_calculator.addition.add(5, 3)
result_2 = my_calculator.substraction.substract(5, 3)

print(result_1)
print(result_2)
'''

'''
---------- 2nd way to import the module ----------

from my_calculator import addition
from my_calculator import substraction

result_1 = addition.add(5, 3)
result_2 = substraction.substract(5, 3)

print(result_1)
print(result_2)
'''
'''
---------- 3rd way to import the module ----------

from my_calculator.addition import add
from my_calculator.substraction import substract

result_1 = add(5, 3)
result_2 = substract(5, 3)

print(result_1)
print(result_2)

'''
from my_calculator import add, substract

result_1 = add(5, 3)
result_2 = substract(5, 3)

print(result_1)
print(result_2)