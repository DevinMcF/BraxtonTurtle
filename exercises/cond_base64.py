def encode_base64(ys):
    digits, s, o, fo, fs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", "", [], [], ""
    for i in str(ys): s = s + ("0" * (8 - len(format(ord(i), 'b')))) + format(ord(i), 'b') if len(format(ord(i), 'b')) < 8 else False
    while s: o.append(s[:6]); s = s[6:]
    o[-1] = o[-1] + "0" * (6 - len(o[-1])) if not len(o[-1]) == 6 else False
    [fo.append(int(binary, 2)) for binary in o]
    for num in fo: fs = fs + digits[int(num)]
    fs = fs + ("=" * (4 - (len(fs) % 4))) if not (len(fs) % 4) == 0 else False
    return fs


print(encode_base64("Pizza"))
