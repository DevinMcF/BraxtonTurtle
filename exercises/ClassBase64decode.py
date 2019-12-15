def base64encode(three_bytes):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    try:
        # turn the three bytes into ints
        b1, b2, b3 = three_bytes[0], three_bytes[1], three_bytes[2]
        # get first 6 bits of b1
        index1 = b1 >> 2
        # join last 2 bits of b1 shifted left 4 with first 4 bits of b2
        index2 = (b1 & 3) << 4 | b2 >> 4
        # join last 4 bits of b2 shifted left 2 with first 2 bits of b3
        index3 = (b2 & 15) << 2 | (b3 & 192) >> 6
        # get last 6 bits of b3
        index4 = b3 & 63
    except (AttributeError, TypeError):
        raise AssertionError('Input should be 3 bytes')
    return f'{digits[index1]}{digits[index2]}{digits[index3]}{digits[index4]}'


def base64decode(four_chars):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    ints = [digits.index(ch) for ch in four_chars]
    b1 = (ints[0] << 2) | ((ints[1] & 48) >> 4)
    b2 = (ints[1] & 15) << 4 | ints[2] >> 2
    b3 = ((ints[2] & 3) << 6) | (ints[3])
    return bytes([b1, b2, b3])
