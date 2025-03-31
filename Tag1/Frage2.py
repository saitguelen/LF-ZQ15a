"""
1.Frage

def func(a,b):
    return a**a

print(func(2)) #TypeError: func() missing 1 required positional argument: 'b'

2. Frage:
x=2
y=6
x +=2**3 #x=8+2=10
x //=y//2//3 #y//2=3//3=1-->10//1=10
print(x) #Ausgabe:x=10

3.Frage:

print('Mike'>'Mikey') #Ausgabe: False

############ 4. Frage:

rates = (1.2, 1.4, 1.0)
new = rates[3:]
for rate in rates[-2:]:
    new += (rate,)
print(len(new))  #Ausgabe :2 new=(1.4, 1.0)

rates = (1.2, 1.4, 1.0)
new = rates[3:]
print(new)  #Ausgabe new=()
for rate in rates[-2:]:
    new += (rate,)
print(len(new))
print(new)

##########################################    5.Frage
The ABC company is building a basketball court

for its employees to improve company morale.

You are creating a Python program that employees

can use to keep track of their average score.

The program must allow users to enter their name and current scores.

The program will output the user name and the user's average score.

The output must meet the following requirements:



The user name must be left-aligned

If the user name has fewer than 20 characters,

additional space must be added to the right

The average score must have three places to the left of the decimal point

and one place to the right of the decimal (xxx.x)



What would you insert instead of ??? and ???
#########################################################

name = input('What is your name?')
sum = 0
score = 0
count = 0
while score != -1:
    score = int(input('Enter your scores: (-1 to end)'))
    if score == -1:
        break
    sum += score
    count += 1
average = sum / count
print('%-20s, your average score is: %4.1f' % (name, average))

%-20s:
%: yüzde ile formatlama başlar

-: sola hizalama

20: toplam genişlik

s: string (metin)

Ortalama puan ise ondalık solunda üç basamak, sağında ise tek basamak şeklinde (xxx.x):


%4.1f
Buradaki 4.1f kullanılır:

4: Toplam uzunluk (3 basamak + nokta dahil 4 karakter, örnek: 123.4)

.1: noktadan sonra bir basamak

f: float (ondalıklı sayı)
########################################      6. Frage
You work for a company that distributes media for all ages.



You are writing a function that assigns a rating based on a user's age.

The function must meet the following requirements:



Anyone 18 years old or older receives a rating of A

Anyone 13 or older, but younger than 18 receives a rating of T

Anyone 12 years old or younger receives a rating of C

If the age is unknown, the rating is set to C


def get_rating(age):
    rating = ''
    if age == None:
        rating = 'C'
    elif age < 13:
        rating = 'C'
    elif age < 18:
        rating = 'T'
    else:
        rating = 'A'
    return rating


print(get_rating(19))  # A
print(get_rating(18))  # A
print(get_rating(17))  # T
print(get_rating(13))  # T
print(get_rating(12))  # C
print(get_rating(11))  # C
print(get_rating(None))  # C
"""



