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

total = 0
for i in range(4):
    if 2 * i < 4:
        total += 1
else:
    total += 1
print(total)

n = 0
if n > 0:
    print("*")
elif n == True:
    print("**")
else:
    print("***")

x = 0
y = 1
x = x ^ y
y = x ^ y
y = x ^ y
print(x, y)


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

data = 'abcdefg'


def func(text):
    del text[2]
    return text


print(func(data))


print(chr(ord('p') + 3))

l1 = [1, 2, 3]

for v in range(len(l1)):
    l1.insert(1, l1[v])

print(l1)  #Ausgabe: [1, 1, 1, 1, 2, 3]


def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))   #9


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