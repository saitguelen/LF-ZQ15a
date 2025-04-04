"""
=========================>1. Frage

def func(x,y):
    if x==y:
        return x
    else:
        return func(x, y-1)

print(func(0,3))

============================>2. Frage

def any():
    print(var + 1, end='')

var = 1
any()
print(var)

##💡 Neden?
any() → print(var + 1) → 2 yazdırır.

print(var) → 1 yazdırır (alt satıra geçmeden devam eder çünkü end='' kullanılmıştı).



===========================>3.Frage

def fun(a,b,c=0):
    sum=a+b+c
    return sum

print(fun(b=0,a=0)) #geht
print(fun(0,1,2)) # geht
print(fun(b=1)) #TypeError: fun() missing 1 required positional argument: 'a'

=======================> 4. Frage


data= {}

def func(d,key, value):
    d[key]=value
    #return d  # eger deger döndürmesini istiyorsak return etmeliyiz ozaman cikti=>{'1': 'Peter'} olur

print(func(data,'1','Peter')) #Ausgabe: None
print(func(data,'2','Patrik'))

===============================>
x="2"
y=2*x
print(y)
=============================>5. Frage



my_list = [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

#Tryityourself:

my_list = [x * x for x in range(5)]
print(my_list)  # [0, 1, 4, 9, 16]
# The same without list comprehension:
my_list = []
for x in range(5):
    my_list.append(x * x)
print(my_list)  # [0, 1, 4, 9, 16]


def fun(lst):
    # del lst[lst[2]]
    del lst[4]
    return lst


print(fun(my_list))  # [0, 1, 4, 9]


=============================>6. Frage

x=float('23.42')
print(bool(x)+True)

#Tryityourself:

x = float('23.42')

print(bool(x) + True)  # 2
print(int(x) + False)  # 23
print(str(x))  # '23.42'
print(bool(x))  # True

print(float('23.42'))  # 23.42
print(bool(23.42))  # True

print(True + True)  # 2
print(True - False)  # 1
print(True * True)  # 1
print(True / True)  # 1.0
print(True % True)  # 0


=============================>7. Frage




print('t' in 'Peter')
print('is' in 'This IS Python Code')

x=['Peter', 'Paul', 'Mary']
y=['Peter', 'Paul', 'Mary']

print(x is y)

print([i for i in range(-1, -2)])  #[]
print([i for i in range(-1, -2,-1)])  #[-1]


=============================>8. Frage


print(not 0)  #True
print(not 23) #False
print(not '') #True
print(not 'Peter')  #False
print(not None) #True

#The values 23 and 'Peter' will evaluate to True and the rest will evaluate to False

print(bool(''))        # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(None))      # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(set()))     # False
print(bool(range(0)))  # False


#=============================>  9. Frage
#How many stars will the following snippet print to the monitor?


i = 4
while i > 0: # i is 4
    i -= 2   # i is 2
    print('*') # *
    if i == 2: #Yip, i is 2
        break  #Leave the loop directly
else:           # Does not apply, because the break got triggered

    print('*') #Ausgabe:*

========================================>  10. Frage:
try:
    print(5 / 0)
    break  #SyntaxError: 'break' outside loop
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")

    There    are    two    syntax    errors:

    break    can    not be    used    outside    of    a    loop,

    and the    default except must    be    last.

"""