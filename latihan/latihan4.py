import binascii
import numpy as np

print(bin(10))
print(hex(710))
# int()

print(int(bin(10), base=0))
print(int(hex(710), base=0))

print(ascii(bin(10)))

# b
arr = [2, 1, 3, 4, 5, 9, 8]
# menentukan  maximum
print(max(arr))
# menentukan minimum
print(min(arr))
# menjumlahkan total
print(sum(arr))
# length
print(len(arr))
print(oct(10))
# char ke desimal ascii
print(ord('c'))
# desimal ke char ascii
print(chr(99))

a = 'cahya'
# f untuk penggabung string
print(f'hallo nama saya {a}\n')


text = b"IGD CAHYA ARI WIBAWA"
# data1 = binascii.b2a_uu(b'aku suma makan')
# print(data1)

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print("**Binary to Ascii**")
print(data_b2a)

# # Converting back from ascii to binary
data_a3b = binascii.a2b_uu(data_b2a)
print("**Ascii to Binary** ")
print(data_a3b)

p = str(bin(ord('c')))
k = str(bin(ord('a')))

print(p)
print(k)
# print(bin(ord(b'c') ^ ord(b'a')))
print(int(bin(ord('c') ^ ord('a')), base=0))
print(chr(int(bin(ord('c') ^ ord('a')), base=0)))
c = bin(ord(b'c') ^ ord(b'a'))
print(c)
# solve
print(bin(int(c, base=0) ^ ord('a')))
# Xor
# print(bin((0b1110 | 0b101) & ~(0b1110 & 0b101)))
# print(bin((ord(b'c') | ord(b'a')) & ~(ord(b'c') & ord(b'a'))))
# np.bitwise_xor()

key = '10'
keys = []
for i in key:
    keys.append(list(bin(ord(i))))

print(ord('0'))
print(keys)

for i in range(0, 16):
    print(keys[i])
