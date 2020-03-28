
arr = 'IGD CAHYA ARI WIBAWA'
key = '10'
# str ke des ke bin


def strbin(arr):
    arrc = []
    for i in arr:
        arrc.append(list(bin(ord(i))))
    return arrc


bint = strbin(arr)
print('biner')


print(bint)

keys = strbin(key)


def looplenstr(l, length):
    loopkey = []
    for i in range(len(length)):
        loopkey.append(l)
    return loopkey


keysb = looplenstr(keys, bint)


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


# print(arrconverted(keysb))

print('batas')

keynya = arrconverted(keysb)


def conarrdes(arr):
    arr1 = []
    for i in arr:
        arr1.append(ord(i))
    return arr1


def xor(p, k):
    c = []
    for i in range(len(p)):
        if p[i]:
            x = int(str(strconverter(p[i])), 0) ^ int(
                str(strconverter(k[i])), 0)

            c.append(chr(x))
    return c


def dexor(c, k):
    p = []
    for i in range(len(c)):
        if c[i]:
            x = int(str(strconverter(c[i])), 0) ^ int(
                str(strconverter(k[i])), 0)
            p.append(chr(x))
    return p


c = xor(bint, keynya)
print(conarrdes(c))
print('cipher')
print(xor(bint, keynya))
print('p cipher')
print(strbin(c))
print('dexor')
ck = strbin(c)
print(dexor(ck, keynya))
