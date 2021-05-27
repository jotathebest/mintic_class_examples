# import <module_name>

import math
print(math.exp(1))

# from <module_name> import <function_name>
from math import exp
print(exp(1))

# from <module_name> import <function_name_1>, ... , <function_name_n>
from math import exp, sqrt
print(sqrt(2))

# from <module_name> import *
from math import *
print(log10(2.0))

# from <module_name> import <function_name_1> as <new_name_1>, ... , <function_name_n> as <new_name_n> 
from math import exp as exponential, sqrt as raiz_cuadrada
print(raiz_cuadrada(2))
