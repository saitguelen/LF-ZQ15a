"""
--->ERSTE fRAGE
date = eval(input('Input: '))
print('Output: ', date)
--->ZWEITE FRAGE
data ={'one':'two','two':'three','three':'one'}
res=data['three']

for _ in range(len(data)):
    res=data[res]

print(res)
--->DRITTE FRAGE
x=1/2+3//3+4**2
print(x)

--->FÜNFTE FRAGE

my_list=[3,1,-2]
print(my_list[my_list[-1]])  #Ausgabe 1

--->SECHSTE FRAGE


def fun(x,y,z):
    return x+2*y+3*z

print(fun(0, z=1, y=3))

--->SIEBSTE FRAGE


def fun(in=2, out=3):
    return in*out

print(fun(3))  # Ausgabe: SyntaxError: invalid syntax in veya out kullanilmaz

--->ACHTE FRAGE

w=bool([False])
print(w)  #Ausgabe:True
s=bool('')
print(s)   #Ausgabe: False
print(w := bool(23))

"""

