# ini adalah sebuah program sederhana mengunakan pyton


# tambah
def tambah(num1, num2):
    return num1 + num2

# kurang


def kurang(num1, num2):
    return num1 - num2
# bagi


def bagi(num1, num2):
    return num1 / num2

# kali


def kali(num1, num2):
    return num1 * num2


print("Makan Pilihan Anda:")
print("1.tambah")
print("2.kurang")
print("3.kali")
print("4.bagi")

pilihan = input("Masukan Inputan Anda : ")

num1 = int(input("Masukan Bilangan Pertama :"))
num2 = int(input("Masukan Bilangan Kedua :"))

if pilihan == '1':
    print(num1, '+', num2, '=', tambah(num1, num2))
elif pilihan =='2':
    print(num1,'-',num2,'=',kurang(num1,num2))

elif  pilihan =='3':
    print(num1,'X',num2,'=',kali(num1,num2))

elif pilihan =='4':
    print(num1,'/',num2,'=',bagi(num1,num2))
else:
    print('inputan anda salah')



