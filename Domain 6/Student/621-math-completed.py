import math

x=3.33
y=-13

print(math.fabs(y))#absolute value[floating absolute]

print(math.ceil(x))#returns the next interger up on the number line after a decimal

print(math.floor(x))#returns an integer w/o a decimal number

print(math.trunc(x))#returns the next highest positive number [towards 0]

print(math.trunc(y))#returns the next lowest negative number [towards 0]

print(math.fmod(y,x))#returns the modulus from divided 2 numbers 

print(math.frexp(x))#returns the mantissa, the fractional part of a log and the 
#exponent of a number
