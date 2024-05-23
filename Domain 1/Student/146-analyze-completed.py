x = 500
y = 200
z = (1,2,3,5,8)
#500/6 = 83 R2
print (x % 6) #What will this result be? 2

#x = 500 * 3 
#x = 1500
x *= 3
print(x) # What will this result be? 1500

print(x > y and x in z) # What will this result be? False
#containment before comparison 
#containment = False 
#one is false so the entire statement is False
print(x/5 > y or y not in z) #What will this result be? True
#"not" over "or"
#1500/5
#300>200 = True 
#Statement is true because one is true
