expression = True and False or True 
step_one = (True and False) or (True)
step_two = (False) or (True)
step_three = True
print(step_three == expression)


# - Booleans -

a = True or False and True  # True
b = False and False or False    # False
c = (True or False) and True    # True
d = True or (True or False and True) and True   # True
e = False or False and False and not False  # False
f = (True or True or False) and True    # True
g = False or (True and False)   # False
h = False and False and False and False and False or True and False # False
i = True or False or True   # True
j = False or (not False)    # True
k = not True or not False   # True
l = False and not False or not False    # True
m = True or not False and True or not not True  # True
n = not not not False   # True
o = not n   # False
p = True or False and not True or (not True and False) and not True or False    # True
q = True or not False or not True or True   # True
r = False and (not True or False or (False or not True and True or False)) and True # False
s = False and not not not True and (False or True or not False) and True or False   # False
t = not (True or False) or not False or (True and False or False)   # True
u = (True or not not False) and (True or (True or (False))) # True
v = False and False or (not False and (not False))  # True
w = (not True or not False) and (not True or (not False))   # True
x = False or False and not True or not False and (not True and False)   # False
y = True and True and True and True and not True and True and True or False # False
z = False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)  # False