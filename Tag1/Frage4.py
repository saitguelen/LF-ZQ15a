"""
=========================> 1. Frage

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)  # Ausgabe: 1 1 2

It does not have practical use, but what also works is

=========================>
c, c = 23, 42

First c becomes 23 and then c becomes 42

You better write

c = 42
=========================>

The same happens in this question in

z, y, z = 1, 1, 2

First z becomes 1 and then z becomes 2

=========================>=========================>

You can also assign the same value to multiple variables:

a = b = c = d = 1
print(a, b, c, d) # 1 1 1 1

=========================>=========================>2. Frage



# The calc_power function calculates exponents
 # x is the base
# y is the exponent # The value of x raised to the y power is returned
def calc_power(x, y):
    comment = "# Return the value"
    return x ** y  # raise x to the y power


print(calc_power(2,6))

#====================================>frage 3
def func1(param):
    return param


def func2(param):
    return param * 2


def func3(param):
    return param + 3

print('##########################################################')
print(func1(func2(func3(1))))

x=1
while x<10:
    print('*', end=' ')

    x= x<<1

###############################frage 4


def fun_1(a):
    return None
def fun_2(a):
    return fun_1(a)*fun_1(a)

print(fun_2(2))  #TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'


print('\\\\')  #Ausgabe: \\
##############################################frage 5
i=0
while i<=5:
    print(i)
    i +=1
    print(i)
    if i%2==0:
        break
    print('*')

i = 0             # Başlangıç
while i <= 5:     # 0 <= 5 ✅

    print(i)      # 👉 0 yazdırır

    i += 1        # i artık 1 oldu!

    print(i)      # 👉 1 yazdırır

    if i % 2 == 0:
        break     # i = 1 olduğundan burası çalışmaz

    print("*")    # 👉 yıldız yazdırılır

"""