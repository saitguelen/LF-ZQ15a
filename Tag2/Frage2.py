
"""

=======================>  1. Frage:


#What is the expected output of the following code?
v = 1


def fun():
    global v
    v = 2
    return v


print(v)


=======================>  2. Frage:
What is the expected output of the following code?





def func1(x):
    return str(x) #1


def func2(x):
    # x=str(x)   #eger bu satiri eklersek x sayi iken string olur ve alacagimiz sonuc 14 yerine 122 olur!!!
    return str(2 * x)  #4



print(func1(1) + func2(2)) #1+4==>14 x string döndügü icin

=======================>  3. Frage:

x = """
from traceback import print_tb
from xml.dom.expatbuilder import FragmentBuilder

"""
print(len(x))

Tryityourself:

x = """
"""
print(len(x))  # 1

# ord() returns an integer representing the Unicode character.
print(ord(x[0]))  # 10 (LF: line feed, new line)

# Same result with single quotes:
y = '''
'''
print(len(y))  # 1

# Every line feed is a character:
z = """

"""
print(len(z))  # 2
Explanation:

In a multiline string the line feed gets saved like any other character.
=======================> 4. Frage:

data= ((1, 2),) * 7
print(len(data[3:8])) #4
print(data) #((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
print(len(data[3:10])) #4


Try it yourself:

# for = 7  # SyntaxError: invalid syntax
# def for(): pass  # SyntaxError: invalid syntax
 
import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for','from', 'global', 'if',
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

"""
#import keyword
#print(keyword.kwlist)

#data = eval(input('Input: '))
#print('Output:', data)

"""
Genel açıklama
Topics: input() eval() list comprehension

Try it yourself:

# data = eval(input('Input: '))
data = eval('[x**2 for x in range(1, 4)]')
print('Input: [x**2 for x in range(1, 4)]')
print('Output:', data)  # Output: [1, 4, 9]
print('----------')
 
# If there is a string in the input,
# it would need quotation marks:
 
# data = eval(input('Input: '))
# data = eval('Hello Python')  # SyntaxError: ...
 
# data = eval(input('Input: '))
data = eval('"Hello Python"')
print('Input: "Hello Python"')
print('Output:', data)  # Hello Python
Explanation:

This question is about the eval() function.

It will evaluate the given code inside of the passed string

Remember input() always returns a string

That works with a number and even the list comprehension.

But to make it work with a string you need to put extra quotation marks around it.

===============================>  5. Frage

my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):  🚫 Ama burada aynı isimle (my_list) bir fonksiyon tanımlanıyor!
                           Bu, listenin üzerine yazıyor, yani artık my_list bir fonksiyon oluyor, liste değil.
    del my_list[3]   #TypeError: 'function' object does not support item deletion  Yani: Bir fonksiyonun indekslerini silemezsin.
    my_list[3] = 'ram' # TypeError: 'function' object does not support item assignment Yani: Bir fonksiyonun 3. indeksine değer atayamazsın, çünkü fonksiyonlarda indeksleme yok.


print(my_list(my_list))

❗️Özet:
Liste ve fonksiyon aynı isme sahip (my_list) olduğu için liste fonksiyonla ezildi.

Sonuçta Python, fonksiyonu bir liste sanıp işlem yapmaya çalışınca hata veriyor.

#################################################################################

#print(float("1,3")) #ValueError: could not convert string to float: '1,3'

#######################################################################################################################

x = [0, 1, 2]
x[0], x[2] = x[2], x[0]

print(x)  #[2, 1, 0]

#####################################################################################################

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)  #[3, 2, 1]

#=====================================================================================0>

data=()
print(data.__len__()) #Ausgabe: 0

print(type(data))  #Ausgabe: <class 'tuple'>

print(len([i for i in range(0,-2)]))

#####################################################################

nums=[1,2,3]
data=('peter',)*(len(nums)-nums[::-1][0])
print(data)  #Ausgabe_: ()


#####################################################################

x=16

while x>0:
    print('*', end=" ")
    x //=2

#####################################################################

x = float(input())     # kullanıcı 2 giriyor → x = 2.0
y = float(input())     # kullanıcı 4 giriyor → y = 4.0

print(y ** (1 / x))    # 4.0 ** (1 / 2.0) → 4.0 ** 0.5 = √4 = 2.0

#####################################################################

def test(x, y=23, z=10):
    print('x is', x, 'and y is', y, 'and z is', z)


test(3, 7)
test(42, z=24)
test(z=60, x=100)

#####################################################################

#{'A': 1, 'B': 2, 'C': 3}




t = (('A', 1), ('B', 2), ('C', 3))
# insert code here
d=dict(t)
print(d)   # Ausgabe: {'A': 1, 'B': 2, 'C': 3}

##################################################################################################################



def fun(n):
    x = []
    for i in range(n):
        x.append(i)
    return x


print(fun(4)) #Ausgabe: [0, 1, 2, 3]

##################################################################################################################

#Expected output:

# [1, 2, 4, 7]


list = [2, 7, 1, 4]

# enter code here
list.sort()
print(list)  #Ausgabe: [1, 2, 4, 7]

##################################################################################################################

sum = count = done = 0
average = 0.0

while done != -1:
    rating =int(input()) # XXX           # ⬅️ Kullanıcıdan giriş alınacak
    if rating == -1:
        break
    sum += rating
    count += 1

average = float(sum / count)

print("Average rating:", round(average, 2)) #YYY + ZZZ                  # ⬅️ Sonuç yazdırılacak
##################################################################################################################

sum = count = done = 0
average = 0.0
while done != -1:
    rating = float(input('Enter next rating (1-5), -1 for done'))
    if rating == -1:
        break
    sum += rating
    count += 1

average = float(sum / count)
print('The average star rating for the new coffee is: '
      + format(average, '.2f'))

# format(average, '.2d') -> ValueError: ...

##################################################################################################################

"""

