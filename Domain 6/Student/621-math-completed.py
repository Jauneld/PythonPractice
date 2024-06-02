import math

#(nan) is a result not a method

x=3.0
y=-13.3

print(math.fabs(y))
"""
absolute value[floating absolute]
"""

print(math.ceil(x))
"""
returns the next interger up on the number line after a decimal
"""

print(math.floor(x))
"""
returns an integer w/o a decimal number
"""

print(math.trunc(x))
"""
returns the next highest positive number [towards 0]
"""

print(math.trunc(y))
"""
returns the next lowest negative number [towards 0]
"""

print(math.fmod(y,x))
"""
returns the modulus from divided 2 numbers
"""

print(math.frexp(x))
"""
returns the mantissa, the fractional part of a log and the 
exponent of a number
"""

print(math.isnan(x))
"""
checks to see if a variable or expression is not a number
and returns true is the expression is not a number and false if the expression
is a number
"""

print(x*y)

print(math.sqrt(x))
"""
returns the square root of a number
"""

print(math.isqrt(x))
"""
returns an integer of a square root of a number
"""

print(math.pow(y,x))
"""
raise the 1nd number to the of the 2nd number
"""

print(math.pi)
"""
returns pi
"""

print(math.pi * math.pow(x,2))
"""
radius of a circle
"""
