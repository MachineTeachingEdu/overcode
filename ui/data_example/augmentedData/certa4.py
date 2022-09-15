import random
random.seed(1)
import numpy
import math
def breakeven():
    return int(math.ceil(math.log(2.5,1.03/1.015)))

from operator import add, mul

def square(x):
   return x * x

def identity(x):
   return x

def triple(x):
   return 3 * x

def increment(x):
   return x + 1
