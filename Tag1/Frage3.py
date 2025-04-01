"""
####################### 1. Frage
for i in range(1,6):
    print(str(i)*5)  #Ausgabe:11111
                            # 22222
                            # 33333
                            # 44444
                            # 55555

###################### 2. Frage

my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)  # Ausgabe: [3, 1, 1]

################## 3. Frage

def function(x=0):
    return x


Burada parametre x için varsayılan değer olarak 0 belirlenmiştir. Bu şu anlama gelir:

Eğer fonksiyon çağrılırken herhangi bir argüman verilmezse, Python otomatik olarak varsayılan değeri (0) kullanır.

İsterseniz kendiniz bir argüman da verebilirsiniz (örneğin function(5)).

Yani bu fonksiyon iki farklı biçimde çağrılabilir:

def function(x=10):
    return x

print(function())        # 0
print(function(7))       # 7
print(function(45+69*58-89*54/2))  #1644.0
# print(function(4, 7))  # TypeError: ...


#############################################   4. Frage

Genel açıklama
Topic: input()



Try it yourself:

value = input("Put anything in!")
print(type(value))  # <class 'str'>

input herzaman string döndürür..

###########################  5. Frage

num = 1


def func():
    num = num + 3  # UnboundLocalError: ... UnboundLocalError: local variable 'num' referenced before assignment
    print(num)


func()

print(num)


#######################  6. Frage---
Genel açıklama
Topics: for if def list input()

Try it yourself:

# Function accepts a list of words from a file,
# and a letter to search for.
# Returns count of the words containing that letter.

def count_letter(letter, word_list):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count


word_list = []
# word_list is populated from a file. Code not shown.
word_list = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']

# letter = input('Which letter would you like to count?')
letter = 'e'

letter_count = count_letter(letter, word_list)

print('There are', letter_count, 'words with the letter', letter)
# There are 3 words with the letter e
Explanation:

for word in word_list:

In every iteration of the for loop,

one element of word_list will be assigned to word

if letter in word:

if the passed letter is in the word

the counter is increased by one.



Q640 (Please refer to this number, if you want to write me about this question.)


========>

Adım Adım Mantığı:
def count_letter(letter, word_list):

Fonksiyon, kullanıcıdan iki değer alır:

letter: aranacak harf

word_list: harfin aranacağı kelime listesi

count = 0

Sayımı tutacak değişken sıfırdan başlar.

for word in word_list:

Listenin her elemanını tek tek dolaşır.

Her turda word değişkeni listedeki yeni bir kelimeye atanır.

if letter in word:

Eğer aranılan harf, şu an kontrol edilen kelimede varsa, altındaki kod çalışır.

count += 1

Harf kelimede bulunduğunda, sayacı bir artırır.

return count

Fonksiyon sonunda sayımı döndürür.

word_list = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']

İçinde arama yapılacak kelime listesi tanımlanmıştır.

letter = 'e'

Aranacak harf 'e' olarak belirlenmiştir. (Gerçek kullanımda input() fonksiyonu ile kullanıcıdan da alınabilir.)

letter_count = count_letter(letter, word_list)

Fonksiyon çağrılır ve dönen sonuç letter_count değişkenine atanır.

print(...)

Sonuç ekrana yazdırılır:

sql
Kopieren
Bearbeiten
There are 3 words with the letter e
Özet Olarak:
Bu kod, verilen bir harfin listedeki kelimelerde kaç kez geçtiğini bulur ve sonucu yazdırır.

for: Listeyi dolaşmak için kullanılır.

if: Koşulu kontrol eder.

def: Fonksiyonu tanımlar.

input(): Kullanıcıdan veri almak içindir (burada yorum içinde bırakılmış, doğrudan değer verilmiş)




############### ==> 7. Frage

##List

nums = [1, 2, 3]
vals = nums
print(nums) #[1, 2, 3]
del vals[1:2]
print(nums)  # [1, 3]
print(vals)  # [1, 3]

=====================> 8. Frage

print(3 * 'abc' + 'xyz')

==============================================>
def func(x, y, z):
    return x + 4 * y + 5 * z
==============================================>

print(func(1, z=2, y=3))


def func(text, num):
    while num > 0:
        print(text)
    num = num - 1

==============================================>
func('Hello', 3)

Explanation:

The incrementation of num needs to be inside of the while loop.

Otherwise the condition num > 0 will never be False

It should look like this:

def func(text, num):
    while num > 0:
        print(text)
        num = num - 1
func('Hello', 3)

Hello
Hello
Hello

=========================================>   9. Frage

d = {'A' : 1, 'B' : 2, 'C' : 3}

d.clear()

print(d)  #{}

Topics: dictionary dict.clear()


=========================================>
Try it yourself:

d = {'A': 1, 'B': 2, 'C': 3}
d.clear()
print(d)  # {}
=========================================>

Explanation:

dict.clear()

The clear() method removes all the elements from a dictionary.

https://www.w3schools.com/python/ref_dictionary_clear.asp

=========================================>=========================================> 10.Frage
Genel açıklama
Topics: def positional/keyword arguments

Try it yourself:

def test(a, b, c, d):
    print(a, b, c, d)


test(1, 2, 3, 4)          # 1 2 3 4
test(a=1, b=2, c=3, d=4)  # 1 2 3 4
test(1, 2, 3, d=4)        # 1 2 3 4

# test(a=1, 2, 3, 4).     # SyntaxError: ...
# test(a=1, b=2, c=3, 4)  # SyntaxError: ...
# test(a=1, 2, c=3, 4)    # SyntaxError: ...

# print(end='', 'Hello')  # SyntaxError: ...
Explanation:

The keyword arguments always have to be at the end.

https://thepythoncodingbook.com/2022/11/11/positional-arguments-and-keyword-arguments-in-python

 """




