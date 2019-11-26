def to_binary(num):
    # """
    # Convert an decimal integer into a string representation of its binary
    # (base2) digits.
    #
    #   >>> to_binary(10)
    #   '1010'
    #   >>> to_binary(12)
    #   '1100'
    #   >>> to_binary(0)
    #   '0'
    #   >>> to_binary(1)
    #   '1'
    # """
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 2))
        num //= 2
    return str(digits[::-1])[1:-1].replace(", ", "")


def to_base3(num):
    """
    Convert an decimal integer into a string representation of its base3
    digits.

      >>> to_base3(10)
      '101'
      >>> to_base3(12)
      '110'
      >>> to_base3(6)
      '20'
    """
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 3))
        num //= 3
    return str(digits[::-1])[1:-1].replace(", ", "")


def to_base4(num):
    """
    Convert an decimal integer into a string representation of its base4
    digits.

      >>> to_base4(20)
      '110'
      >>> to_base4(28)
      '130'
      >>> to_base4(3)
      '3'
    """
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % 4))
        num //= 4
    return str(digits[::-1])[1:-1].replace(", ", "")


def to_base(num, base):
    """
    Convert an decimal integer into a string representation of the digits
    representing the number in the base (between 2 and 10) provided.

      >>> to_base(10, 3)
      '101'
      >>> to_base(11, 2)
      '1011'
      >>> to_base(10, 6)
      '14'
    """
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return str(digits[::-1])[1:-1].replace(", ", "")


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
