"""

employees = []

# for i in range(1, 196):
for i in range(1, 8):  # Just for convenience
    employees.append('Employee' + str(i))

for i in range(1, 8):
    employees.append('Manager' + str(i))

print(employees)
print(employees[:-5])
print(employees[0:-5])
print(employees[1:-4])
# One manager present and one employee is missing
print(employees[1:-5])  # One employee is missing
print(employees[0:-4])  # One manager present

======================================================================>
total = 0
for i in range(4):
    if 2 * i < 4:
        total += 1
else:
    total += 1
print(total)


======================================================================>


n = 0
if n > 0:
    print("*")
elif n == True:
    print("**")
else:
    print("***")

======================================================================>


x = 0
y = 1
x = x ^ y
y = x ^ y
y = x ^ y
print(x, y)


======================================================================>

def func(p1, p2):
    p1 = 1
    p2[0] = 42


x = 3
y = [1, 2, 3]
print(y[0])

func(x, y)
print(y[0])
print(x, y[0])
print(y[0])
======================================================================>
data = 'abcdefg'


def func(text):
    del text[2]
    return text


print(func(data))

======================================================================>
print(chr(ord('p') + 3))
======================================================================>
l1 = [1, 2, 3]

for v in range(len(l1)):
    l1.insert(1, l1[v])

print(l1)  #Ausgabe: [1, 1, 1, 1, 2, 3]
======================================================================>

def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))   #9

======================================================================>
"""
list = ['Peter', 'Paul', 'Mary']

def func(data):
#def list(data):
    del data[1]
    data[1] = 'Jane'
    return data

print(func(list))

#print(list(list))

#funktion ve liste ayni isim olamaz

#x = input('Enter the first number: ')   # Örn: "2"
#y = input('Enter the second number: ')  # Örn: "3"

#print('The Result is ' + str(int(x) + int(y)))  # Çıktı: The Result is 5
"""
def func(num):
    res = '*'
    for _ in range(num):
        res += res
    return res


for x in func(5):
    print(x, end='_') #Ausgabe: *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
                            # yani  2**5=32 tane yildiz yapar
======================================================================>
print()

x=4.5
y=2
print(x//y)
======================================================================>
d = {}
d[1] = 1
print(d)
d['1'] = 2
print(d)
print()
d[1] += 1
print(d)
sum = 0

for k in d:
    sum += d[k]

print(sum)

======================================================================>
def func(x):
    return 1 if x % 2 != 0 else 2


print(func(func(1)))

======================================================================>


list1 = ['Peter', 'Paul', 'Mary', 'Jane']
list2 = ['Peter', 'Paul', 'Mary', 'Jane']

print(list1 is not list2)  #true
print(list1 != list2)           #false
print(id(list1))  #2060070818752
print(id(list2))  #2060070818688 farkli id


list1 = list2

print(id(list1))  #2243187250048
print(id(list2))  #2243187250048 ayni id

print(list1 is not list2) #false
print(list1 != list2)     #false

======================================================================>
z = y = x = 1
print(x, y, z, sep='*')  #Ausgabe: 1*1*1

a = 10
b = 20
c = a > b
print(not(c))

======================================================================>

x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res


print(func(x[0]))

my_list = [3, 1, -2]
print(my_list[my_list[-1]])
======================================================================>



def func(x, y=2):
    num = 1
    for i in range(y):
        num = num * x
    return num


print(func(4))
print(func(4, 4))

======================================================================>
def fun():
    return 3


def add(n):
    return fun() + n


print(add(3))


======================================================================>



x = input()
y = input()
print(x + y)
======================================================================>

nums = [3, 7, 23, 42]
alphas = ['p', 'p', 'm', 'j']

print(nums is alphas)  #False
print(nums == alphas)  #False

nums = alphas

print(nums is alphas)  #True
print(nums == alphas)   #True
======================================================================>
str = 'Hello World'
print(str[::-1])

======================================================================>



x = 1

if x > 0 or x < 1:
    print("1")
if x > 1:
    print("2")
elif x >= 1:
    print("3")
else:
    print("4")

======================================================================>

floor = 10
while floor != 0:
    floor //= 4
    print("*", end="")
    #print(floor)
else:
    print("*")

======================================================================>
  
  

x = '\''
print(len(x))# Ausgabe: 1

num = 1

======================================================================>

def func():
    num = 3
    print(num, end=' ')


func()

print(num)
======================================================================>




def func1(a):
    return a ** a


def func2(a):
    return func1(a) * func1(a)


print(func2(2))  #Ausgabe: 16
=====================================================================>


t1 = (1, 4, 9)
t2 = ('A', 'D', 'Z')
t3 = (True, False, None)
t4 = (5.0, 7.5, 9.9)

t1, t3 = t2, t4
print(t1)   #Ausgabe: ('A', 'D', 'Z')


=====================================================================>


x = input()
y = int(input())

print(x * y)  #333333

=====================================================================>

"""