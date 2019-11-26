def to_binary(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits = str(num % 2) + digits
        num //= 2
    return digits


def to_base3(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits = str(num % 3) + digits
        num //= 3
    return digits


def to_base4(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits = str(num % 4) + digits
        num //= 4
    return digits


def to_base(num, base):
    if num == 0:
        return [0]
    digits = ""
    while num:
        digits = str(num % base) + digits
        num //= base
    return digits
