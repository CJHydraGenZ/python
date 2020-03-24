import json
import datetime

x = datetime.datetime.now()

print(x)


def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(2, 2, 2))


# lambda
# x = lambda a,b : a + b
# print(x(4,4))

# function lambda
def tambah(n):
    return lambda a: a + n


tambahLan = tambah(4)
print(tambahLan(4))
print(tambah(2)(2))


# for x in "banana":
#   print(x)
print('batas')
# range(mulai dari,batas nilai,kelipatan)
# for x in range(2, 30, 3):
#     print(x)
for x in range(0, 20, 2):
    print(x)

# remove duplikat number
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# dengan functon


def my_function(x):
    return list(dict.fromkeys(x))


mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

# reverses string
txt = "Hello World"[::-1]
print(txt)


def my_function(x):
    return x[::-1]


mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)


