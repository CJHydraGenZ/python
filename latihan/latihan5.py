
arr = 'IGD CAHYA ARI WIBAWA'
key = '10'
# str ke des ke bin
bint = []
print('biner')
for i in arr:
    # print(bin(ord(i)))
    bint.append(list(bin(ord(i))))

print(bint)

keys = []
for i in key:
    keys.append(list(bin(ord(i))))


print(len(bint))
print('keys')

keysb = []
for i in range(len(bint)):
    # print(keys)

    keysb.append(keys)
    # keysb.fromkeys(dict(keys))

print(len(keysb))
# print(keysb)
# a = np.bitwise_xor(bint[0], keysb[0])
# c = bin(bint ^ keysb)
# print(c)
# print(int(bin(ord('c') ^ ord('a')), base=0))
# print()
# print('gabungam')
# ab = [a for a in bint+keysb if (a not in bint) or (a not in keysb)]
# print(ab)


def strconverter(s):
    str1 = ""
    for x in s:
        str1 += x
    return str1


def arrconverted(ar):
    arc = []
    for i in ar:
        for j in i:
            arc.append(j)
    return arc


print(arrconverted(keysb))

print('batas')
# print(arrconverted(len(keysb), bint, keysb))
# print(arrconverted(bint, keysb))


# def xor(p, k):
#     xorr = []
#     for i in range(len(bint)):
#         if p[i] == k[i]:
#             x = int(p, base=36) ^ int(k, base=36)
#             print(x)
#             xorr.append(x)
#             # for i in k:
#             #     print(i)
#     return xorr
keynya = arrconverted(keysb)
c = []
for i in range(len(bint)):
    # print(len(bint))
    if bint[i]:
        x = int(str(strconverter(bint[i])), 0) ^ int(
            str(strconverter(keynya[i])), 0)
        c.append(chr(x))
        # print(chr(x))
print('cipher')
print(c)
# print('batas asas')
# for i in range(len(keysb)):
#     print(keysb[i])
#     print(len(keysb))

# a = strconverter(arrconverted(bint))
# b = strconverter(arrconverted(keysb))
# print('a')
# # print(len(a))
# print('b')
# # print(len(b))
# print('c')
# c = xor(a, b)
# print(c)
# bint2 = []
# for i in bint:
#     # se += i
#     for j in i:
#         # print(j)
#         bint2.append(j)
#     # print(i)

# print(arrconverted(bint))
# a = arrconverted(bint)
# b = arrconverted(keysb)
# c = strconverter(a)
# d = strconverter(b)
# e = int(c, base=0) ^ int(d, base=0)

# # a = "11011111101100110110011001011101000"
# # b = "11001011101100111000011100001100001"
# # y = int(a,2) ^ int(b,2)
# # print '{0:b}'.format(y)
# print(bin(e))
# print(b)

# print(se)
# for i in bint:
#     liststring =
#     print(i)
# res = reduce(bint ^ keysb)
# print(res)
# print(converter(bint))
