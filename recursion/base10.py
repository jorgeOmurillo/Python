def toSrt(n, base):
    convertString = '0123456789ABCDEF'

    if n < base:
        return convertString[n]

    else:
        return toSrt(n//base, base) + convertString[n%base]

print toSrt(1000, 16)
