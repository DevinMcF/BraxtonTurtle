def base64clean(ascii):
    bytelist = []
    o = []
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    while ascii:
        o.append(ascii[:4])
        ascii = ascii[4:]
    for six in o:
        ints = [digits.index(ch) for ch in six]
        print(ints)
        b1 = (ints[0] << 2) | ((ints[1] & 48) >> 4)
        b2 = (ints[1] & 15) << 4 | ints[2] >> 2
        b3 = ((ints[2] & 3) << 6) | (ints[3])
        print([b1, b2, b3])
        bytelist.extend([bin(b1), bin(b2), bin(b3)])
    return bytelist

print(base64clean("Test"))
