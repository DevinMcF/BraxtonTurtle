def to_binary(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 2))
        num //= 2
    digits = ''.join(str(x) for x in digits[::-1])
    return digits


def to_base3(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 3))
        num //= 3
    digits = ''.join(str(x) for x in digits[::-1])
    return digits


def to_base4(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 4))
        num //= 4
    digits = ''.join(str(x) for x in digits[::-1])
    return digits


def to_base(num, base):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    digits = ''.join(str(x) for x in digits[::-1])
    return digits
