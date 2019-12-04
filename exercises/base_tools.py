def to_binary(num):
    if num == 0:
        return "0"
    digits = ""
    while num:
        digits = str(num % 2) + digits
        num //= 2
    return digits


def to_base3(num):
    if num == 0:
        return "0"
    digits = ""
    while num:
        digits = str(num % 3) + digits
        num //= 3
    return digits


def to_base4(num):
    if num == 0:
        return "0"
    digits = ""
    while num:
        digits = str(num % 4) + digits
        num //= 4
    return digits


# Max 36
def to_base(num, base):
    if num == 0:
        return "0"
    numstr = ""
    while num:
        numstr = chr((num % base)+55) + numstr
        num //= base
    return numstr


def to_base64num(num):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if num == 0:
        return "0"
    numstr = ""
    while num:
        numstr = digits[num % 64] + numstr
        num //= 64
    return numstr


def encode_base64(ys):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    test_str = str(ys)
    s = ""
    for i in test_str:
        i = format(ord(i), 'b')
        if len(i) < 8:
            i = ("0" * (8-len(i))) + i
        s = s + i
    o = []
    fo = []
    fs = ""
    while s:
        o.append(s[:6])
        s = s[6:]
    if not len(o[-1]) == 6:
        o[-1] = o[-1] + "0"*(6-len(o[-1]))
    for binary in o:
        i = int(binary, 2)
        fo.append(i)
    for num in fo:
        fs = fs + digits[num]
    fs = fs + ("=" * (4 - (len(fs) % 4)))
    return fs


def spliter(word):
    return [char for char in word]


def decode_base64(ys):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    test_str = str(ys).replace('=', "")
    strlist = spliter(test_str)
    bins = ""
    o = []
    fo = []
    for s in strlist:
        loc = digits.find(s)
        loc = format(loc, 'b')
        if len(loc) < 6:
            loc = str(loc)
            loc = ("0" * (6 - len(loc))) + loc
        bins = bins + loc
    while bins:
        o.append(bins[:8])
        bins = bins[8:]
    for s in o:
        if len(s) == 8:
            fo.append(s)
    fs = ''.join([chr(int(binary, 2)) for binary in fo])
    return fs
