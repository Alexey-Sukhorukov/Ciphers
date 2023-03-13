from math import gcd
from sympy import mod_inverse
from random import randint


p, q = 17, 11
n = p * q
f = (p - 1) * (q - 1)


for e in range(11, f):
    if gcd(e, f) == 1:
        break