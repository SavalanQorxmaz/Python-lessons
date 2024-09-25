print(hash(5))
print(id(5))
print(hash('s'))
print(id('s'))
my_set = {()}
print(type(my_set))
# print(hash(my_set))
my_set = {()}
my_tuple = ({})
print(type(my_tuple))
x = set((1, 2, 3))
print(x)
y = list((1, 2, 3))
print(y)
z = dict({'x': 5, 'y': 6})
print(z)
t = tuple((1, 2, 3))
print(t)
d = {
    1: 1,
    's':'d',
    (1, 2, 3): (2, 4, 6),
     }
print(d)
if type(my_set) is set:
    print('yes')
    if type(t) is tuple:
        print('Yes, tuple')
print(type(d.values())) 
if str(type(d.values())) == '<class \'dict_values\'>':
    print('Yes list')

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Charles"]
b1 = ["Jenny", "Christy", "Monica", "Charles"]

a.extend([None for x in range(len(b)-len(a)) ])
print(a)
for x in zip(a, b):
    print(x)
ab = list(zip(a, b))
print(ab)

c, *d = zip(*list(zip(a, b,b1)))
print(c)
print(d)
