"""
data = (1,) * 3
#data[0] = 2   #TypeError: 'tuple' object does not support item assignment
print(data)
list=[]
for i in range(data):
    list.insert(i)
print(list)
list[0]=2
print(list)

#================================================================================>

x=16
while x>0:
    print('*')
    x //=2

#================================================================================>

foo = (1, 2, 3)
foo.index(0)  #ValueError: tuple.index(x): x not in tuple

#================================================================================>

foo = (1, 2, 3)
print(foo.index(5)) #ValueError: tuple.index(x): x not in tuple


foo = (1, 2, 3)
print(foo.index(1)) #0
print(foo.index(2))  #1
print(foo.index(3))  #2


#================================================================================>

L = [i for i in range(-1, -2)]

print(L)   #[]

k = [i for i in range(0,10)]

print(k)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#================================================================================>

data = [[3 - i for i in range(3)] for j in range(3)]
print(data)  # [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
res = 0

for i in range(3):
    print('data[' + str(i) + '][' + str(i) + ']: ', data[i][i])

    #data[0][0]: 3
    #data[1][1]: 2
    #data[2][2]: 1

    res += data[i][i]

print(res)  # 6 (3 + 2 + 1)

#================================================================================>


nums = [1, 2, 3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)


#================================================================================>

nums = [1, 2, 3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)  # ()

print(len(nums) - nums[::-1][0])  # 0
print(len([1, 2, 3]) - [1, 2, 3][::-1][0])  # 0
print(3 - [3, 2, 1][0])  # 0
print(3 - 3)  # 0
print(0)  # 0

print(('Peter',))  # ('Peter',)
print(type(('Peter',)))  # <class 'tuple'>
print(type('Peter'))  # <class 'str'>
print(('Peter',) * 0)  # ()
print((1, 2, 3) * 0)  # ()

##===============================================================================>



def any():
    print(var + 1, end='')


var = 1
any()
print(var)


#================================================================================>


data = [1, {}, (2,), (), {3}, [4, 5]]
points = 0

for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 10
    elif type(data[i]) == set:
        points += 100
    elif type(data[i]) == dict:
        points += 1000
    else:
        points += 10000

print(points)


#================================================================================>


data = [[x for x in range(y)] for y in range(3)]
print(data)

for d in data:
    if len(d) < 2:
        print('*')



data = ()
print(data.__len__())

#================================================================================>


order = int(input('Please enter the order value: '))
state = input('Please enter the state (as postal abbreviation): ')
delivery = 0

if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
if state in ['GA', 'WV', 'FL']:
    if order > 1000:
        delivery += 30
    if order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 25
print(delivery)


#================================================================================>


data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    if len(d) == 4:    #len('Paul=4, mary=4, jane=4)
        print(d)
        #print(len(d))


#================================================================================>



nums = [1, 2, 3]
vals = nums
del vals[:]
print(vals)  #[]
print(nums)  #[]


#================================================================================>


data = {'z': 23, 'x': 7, 'y': 42}

for _ in sorted(data):
    print(data[_], end=' ')  #7 42 23


#================================================================================>

# Code-1
num=42
if num % 2 == 0:
    even = True
else:
    even = False

# Code-2
even = True if num % 2 == 0 else False

# Code-3
even = num % 2 == 0


#================================================================================>

my_list = [0 for i in range(1, 3)]
print(my_list)  #[0, 0]


my_list2 = [2 for i in range(1, 3)]
print(my_list2)  #[2, 2]

my_list1 = [1 for i in range(1, 3)]
print(my_list1)  #[1, 1]

my_list10 = ['A' for i in range(1, 3)]
print(my_list10)  #['A', 'A']

my_list11 = [[1,2,3] for i in range(1, 3)]
print(my_list11)  #[[1, 2, 3], [1, 2, 3]]

#================================================================================>

x = 1


def a(x):
    return 2 * x


x = 2 + a(x)  # Line 8
print(a(x))  # Line 9


#================================================================================>

x = (1, 4, 7, 9, 10, 11)
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
res = 1
for z in x:
    if z in y:
        res += z
print(res)

#================================================================================>

data = [[42, 17, 23, 13], [11, 9, 3, 7]]
res = data[0][0]
for da in data:
    for d in da:
        if res > d:
            res = d
print(res)

data = [[42, 17, 23, 13], [11, 9, 3, 7]]
res = data[0][0]
print(res)  # 42
for da in data:
    for d in da:
        if res > d:
            print('d: ', d)  # 17 -> 13 -> 11 -> 9 -> 3
            res = d


#================================================================================>



data1 = 'a', 'b'
data2 = ('a', 'b')
print(data1 == data2)

print(type(+1E10))  #<class 'float'>
print(type(5.0))  #<class 'float'>
print(type('True'))  #<class 'str'>
print(type(False))  #<class 'bool'>


#================================================================================>

str1 = 'Peter'
str2 = str1[:]
print(id(str2))  #3137062269808
print(id(str1))  #3137062269808

#================================================================================>


x = 23 + 42
y = '23' + '42'
z = '23' * 7

print(type(x))  #int
print(type(y))  #str
print(type(z))  #str


#================================================================================>

marks = [80, 70, 90, 90, 80, 100]

average = sum(marks) // len(marks)

grade = ''

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 65 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print(grade)  #b


#================================================================================>

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
while x < 10:        # Line 3
    #print(nums(x))   # Line 4
    if nums[x] == 7:  # Line 5
        break        # Line 6
    else:            # Line 7
        x += 1       # Line 8



#================================================================================>

data = {'Peter': 30, 'Paul': 31}
print(list(data.keys()))   #['Peter', 'Paul']



#================================================================================>

data = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
count = 0

for i in range(len(data)):
    if type(data[i]) == list:
        count += 1

print(count)


#================================================================================>

try:
    raise Exception
except BaseException:
    print('1')
except Exception:
    print('2')
except:
    print('3')


#================================================================================>

data1 = '1', '2'
data2 = ('3', '4')
print(data1 + data2)

data = (1, 2, 4, 8)
data = data[-2:-1]
data = data[-1]
print(data)

#================================================================================>

data = {'name': 'Peter', 'age': 30}
person = data.copy()
print(id(data) == id(person))
print(person)
print(id(data))
print(id(person))

#================================================================================>

def func(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in func(3):
    print(x, end='')

#================================================================================>

x = 42


def func():
    global x
    print('1. x:', x)
    x = 23
    print('2. x:', x)


func()
print('3. x:', x)

#1. x: 42
#2. x: 23
#3. x: 23

#================================================================================>
"""


