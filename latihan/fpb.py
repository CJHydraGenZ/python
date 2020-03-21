# fpb mengunakan python


def hitung_fpb(x, y):
    # memilih bilangan terkecil
    if x > y:
        terkecil = y
    else:
        terkecil = x

    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i

    return fpb


num1 = 96
num2 = 24
print('Looping')
print('FPB dari', num1, 'dan', num2, '=', hitung_fpb(num1, num2))


# algoritma Euclidean
def hitung_fpbAE(x, y):
    while (y):
        x, y = y, x % y
    return x


print('algoritma Euclidean')
print('FPB dari', num1, 'dan', num2, '=', hitung_fpbAE(num1, num2))
