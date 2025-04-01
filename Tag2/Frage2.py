
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

"""