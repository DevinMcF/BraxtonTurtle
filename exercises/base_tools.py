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


def to_base64(num):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if num == 0:
        return "0"
    numstr = ""
    while num:
        numstr = digits[num % 64] + numstr
        num //= 64
    return numstr


print(to_base64(65535))
