import random
random.seed(1)
import numpy
def breakeven():
    anos=0
    pop_a=80000
    pop_b=200000
    taxa_a=1.03
    taxa_b=1.015
    while pop_a<pop_b:
        pop_a*=taxa_a
        pop_b*=taxa_b
        anos+=1
    return anos

from operator import add, mul

def square(x):
   return x * x

def identity(x):
   return x

def triple(x):
   return 3 * x

def increment(x):
   return x + 1
