import math


# pangkat 2


def pangkat(num1, num2):
    return math.floor(math.pow(num1, num2))


# print('pangkat : ', pangkat(2, 3))

arr = [1, 2, 3, 4, 5, 5]

for i in arr:
    print(i + pangkat(i, 2))
