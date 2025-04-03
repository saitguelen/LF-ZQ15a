"""
x = 1
y = 2
z = x
x = y
y = z
print(x, y)

===================================================================>

languages = ['English', 'Spanish', 'German']
more_languages = ['English', 'Spanish', 'German']
extra_languages = more_languages

print(more_languages is extra_languages)  #True
print(languages==more_languages)        #True
print(languages is more_languages)     #'false'

print(languages is extra_languages)       # False
print(id(languages))         #2461056673984
print(id(more_languages))       #2461056659904
print(id(extra_languages))      #2461056659904


===================================================================>


w = [7, 3, 23, 42]
x = w[1:]
y = w[1:]
z = w
y[0] = 10
z[1] = 20
print(w)

===================================================================>


x = 1
print(++++x)  #1

tup = (1, ) + (1, )
tup = tup + tup
print(tup)  #(1, 1, 1, 1)
print(len(tup))  #4


===================================================================>

x = int(input())
y = int(input())
x = x % y
print(x)  #x=3
x = x % y
print(x) #x=3
y = y % x
print(y)  #y=1

===================================================================>


def func(data):
    for d in data[::2]:
        yield d


for x in func('abcdef'):
    print(x, end='')


===================================================================>

list = ['A', 2, 7, 1, 4]
list.reverse()
# enter code here

print(list)


===================================================================>



print('Peter' 'Wellert')

data = [4, 2, 3, 2, 1]
res = data[0]

for d in data:
    if d < res:
        res = d

print(res)
===================================================================>




data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(0, 4):
    print(data[i].pop(), end=' ')


===================================================================>



dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i],)

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])
    # Insert your code here.

===================================================================>




data = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    data[i - 1] = data[i]

for i in range(0, 6):
    print(data[i], end=' ')
print()

===================================================================>#


x = '\\\\'
print(len(x))
print(x)

===================================================================>


n = 1
if n == 1:
    print("*")
if n == True:
    print("**")
if n == False:
    print("***")


===================================================================>


data = {'1': '0', '0': '1'}

for d in data.vals():  # AttributeError: ...
    print(d, end=' ')

===================================================================>

x = 0
while x < 6:
    print('1. x:', x)         # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    x += 1
    print('2. x:', x)         # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    if x % 2 == 0:
        print('x in if:', x)  # 2 -> 4 -> 6
        continue
    print('x behind if:', x)  # 1 -> 3 -> 5
    print('*')


===================================================================>



data = [[0, 1, 2, 3] for i in range(2)]
#print(data[2][0])  # # IndexError: list index out of range

print(data)
print(data[0])
print(data[1])
print(data[0][2])
print(data[1][3])
print(data[0][0])

===================================================================>



print(float('1.3'))  #Ausgabe: 1.3


===================================================================>

def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)
  # TypeError: unsupported operand type(s) for *:
    # NoneType' and 'NoneType


print(function_2(2))

===================================================================>




data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(len(data))  # 4

print(type(data))  # <class 'set'>
print(data)  # {1, 2, 3, 4}

# Also works directly:
print(len({1, 2, 2, 3, 3, 3, 4, 4, 4, 4}))  # 4

===================================================================>

x = 16
while x > 0:
    print('*', end=" ")
    x = x >> 1
    print(x, end=" ")  #* 8 * 4 * 2 * 1 * 0

===================================================================>

x = 1
while x < 10:
    print('*')
    x = x << 1  #2  * 4 *   8 *  16

===================================================================>




print(chr(ord('z') - 2))   # Ausgabe: x


data = ()
print(data.__len__())

===================================================================>

data = {'a': 1, 'b': 2, 'c': 3}
print(data['a'], data['b'])  #Ausgabe: 1 2
#print(data['a', 'b'])  #Ausgabe: Type Error


===================================================================>

print(len([i for i in range(0, -2)]))

===================================================================>


def func(item):
    item += [1]


data = [1, 2, 3, 4]
func(data)
print(len(data))
print(data)   #Ausgabe: [1, 2, 3, 4, 1]
===================================================================>




def func(x):
    global y
    y = x * x
    return y


func(2)
print(y)


===================================================================>


for i in range(1):
    print('#')
    print(i)
else:
    print('#')
    print(i)


===================================================================>


my_list1=[1,2,3]
my_list2=[]
for v in my_list1:
    my_list2.insert(0,v)
    print(my_list2)


===================================================================>

vals=[0,1,2]
vals[0],vals[2]=vals[2], vals[0]
print(vals[0])
print(vals[2])
print(vals)

===================================================================>

"""

