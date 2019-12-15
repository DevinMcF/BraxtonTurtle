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
        return "A"
    numstr = ""
    while num:
        numstr = digits[(num % 64) - 1] + numstr
        num //= 64
    return numstr


def encode_base64(ys):
    # Base64 Digits
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Makes sure the input is a string.
    test_str = str(ys)
    # Defining blank variables
    s, o, fo, fs = "", [], [], ""
    # Goes through all of the characters in the string.
    for i in test_str:
        # Turns the character into ascii binary
        i = format(ord(i), 'b')
        # This bit just adds the zeros to the beginning that got trimmed off
        if len(i) < 8:
            i = ("0" * (8-len(i))) + i
        # Turns it into a string
        s = s + i
    # This splits the string of binary values into a list with each item being 6 digits (binary for Base64)
    while s:
        o.append(s[:6])
        s = s[6:]
    # This adds 0's at the end if the final item in the list doesn't have the necessary 6 digits.
    if not len(o[-1]) == 6:
        o[-1] = o[-1] + "0"*(6-len(o[-1]))
    # Single line for loop to turn binary into integers.
    for binary in o:
        fo.append(int(binary, 2))
    # Grabs the digit that is assigned to the integer and adds it to final string.
    for num in fo:
        fs = fs + digits[int(num)]
    # Adds padding if the line is not long enough.
    if not (len(fs) % 4) == 0:
        fs = fs + ("=" * (4 - (len(fs) % 4)))
    return fs


def decode_base64(ys):
    # Base64 Digits
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Take string, remove padding
    test_str = str(ys).replace('=', "")
    # Create the blank variables
    bins, o, fo = "", [], []
    # Go through the characters in the word.
    for s in test_str:
        # Find the decimal number for the digit
        loc = digits.find(s)
        # Turn the decimal number into a binary representation
        loc = format(loc, 'b')
        # This bit just adds the zeros to the beginning that got trimmed off
        if len(loc) < 6:
            loc = str(loc)
            loc = ("0" * (6 - len(loc))) + loc
        # Then you create a string of all the binary values
        bins = bins + loc
    # This splits the string of binary values into a list with each item being 8 digits (binary for ascii)
    while bins:
        o.append(bins[:8])
        bins = bins[8:]
    # This removes the leftover item that isn't a letter (The 0's added to the end by Base64)
    for s in o:
        if len(s) == 8:
            fo.append(s)
    # This turns all of the binary numbers into ascii characters and then makes them a string.
    fs = ''.join([chr(int(binary, 2)) for binary in fo])
    return fs


def base64encode(three_bytes):
    """
      >>> base64encode(b'\\x5A\\x2B\\xE6')
      'Wivm'
      >>> base64encode(b'\\x49\\x33\\x8F')
      'STOP'
      >>> base64encode(b'\\xFF\\xFF\\xFF')
      '////'
      >>> base64encode(b'\\x00\\x00\\x00')
      'AAAA'
    """
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
