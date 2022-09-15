import random
random.seed(1)
import numpy
def breakeven():
    years=0
    population_a=80000
    population_b=200000
    rate_a=0.03
    rate_b=0.015
    while population_a<population_b:
        population_a=population_a+population_a*rate_a
        population_b=population_b+population_b*rate_b
        years+=1
    return years

from operator import add, mul

def square(x):
   return x * x

def identity(x):
   return x

def triple(x):
   return 3 * x

def increment(x):
   return x + 1
