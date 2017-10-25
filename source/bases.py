#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def letters(number):
    number

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    total = 0

    # List of all digits
    fulldigit = list(digits)

    for value, digit in enumerate(digits):
        if digit.isalpha():
            number = ord(digit)-87
            total += number * (base**(len(fulldigit)-value-1))
            # Put error checking here; not within range of base
        else:
            total += int(digit) * (base**(len(fulldigit)-value-1))
    return total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    total = ""
    count = 0

    # how far do we go?
    while True:
        result = number // (base**(count+1))
        if result == 0:
            break
        count += 1
    for i in range(count, -1, -1):
        newresult = divmod(number, base**i)
        number = newresult[1]

        if newresult[0] >= 10:
            total = total+chr(87+(newresult[0]))
        else:
            total = total+(str(newresult[0]))
    return total


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    total = 0
    finaltally = ""
    digits = list(digits)

    for value, number in enumerate(digits):
        if number.isalpha():
            digits[value] = ord(number) - 87

    for number in digits:
        total = (base1 * total) + int(number)

    while total > 0:
        remainder = total % base2
        if remainder >= 10:
            remainder = chr(87 + remainder)
        finaltally = str(remainder) + finaltally
        total = total // base2

    return finaltally

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        print("Working on it")
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    if len(args) == 2:
        digits = int(args[0])
        base1 = int(args[1])
        result = encode(digits, base1)
        # print('{} in base 10 is {} in base {}'.format(digits, result, base1))

    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
