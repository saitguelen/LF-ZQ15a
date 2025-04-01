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
"""



