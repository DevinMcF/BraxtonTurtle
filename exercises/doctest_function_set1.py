def only_evens(nums):
    """
      >>> only_evens([3, 8, 5, 4, 12, 7, 2])
      [8, 4, 12, 2]
      >>> my_nums = [4, 7, 19, 22, 42]
      >>> only_evens(my_nums)
      [4, 22, 42]
      >>> my_nums
      [4, 7, 19, 22, 42]
    """
    for num in nums:
        if num % 2 == 0:
            try:
                evens.append(num)
            except:
                evens = [num]
    return evens


def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    nums = list(str(n))
    count = 0
    for num in nums:
        if int(num) % 2 == 0:
            count += 1
    return count


def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    nums = list(str(n))
    for num in nums:
        try:
            squares.append(int(num) ** 2)
        except:
            squares = [int(num) ** 2]
    return sum(squares)


def lots_of_letters(word):
    """
      >>> lots_of_letters('Lidia')
      'Liidddiiiiaaaaa'
      >>> lots_of_letters('Python')
      'Pyyttthhhhooooonnnnnn'
      >>> lots_of_letters('')
      ''
      >>> lots_of_letters('1')
      '1'
    """
    letters = list(word)
    new_word = ""
    count = 1
    for letter in letters:
        letter = letter*count
        new_word = new_word + letter
        count += 1
    return new_word


def gcf(m, n):
    """
          >>> gcf(10, 25)
          5
          >>> gcf(8, 12)
          4
          >>> gcf(5, 12)
          1
          >>> gcf(24, 12)
          12
        """
    while n != 0:
        m, n = n, m % n
    return m


def is_prime(n):
    """
          >>> is_prime(5)
          True
          >>> is_prime(98)
          False
          >>> is_prime(4000)
          False
        """
    a = [x for x in range(2, n) if n % x == 0]
    if n <= 1:
        prime = False
    elif len(a) == 0:
        prime = True
    else:
        prime = False
    return prime


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
