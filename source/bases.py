#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# We default to lcase for printing
UCASE_ASCII = 55
LCASE_ASCII = 87
BASE_DIGITS = string.digits + string.ascii_letters

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    total = 0

    # Turn digits into lists
    digits = list(digits)

    # Keep adding up the digits to build up proper number representation
    # If letter, turn it into corresponding number
    # CURRENT CHECKS: upper or lower, if too high for base (using 3 in base3)
    for number in digits:
        if number not in BASE_DIGITS:
            raise ValueError("'{}' is an illegal character.".format(number))
        if str(number).islower():
            number = ord(number) - LCASE_ASCII
        if str(number).isupper():
            number = ord(number) - UCASE_ASCII
        if int(number) >= base:
            raise ValueError("Input must be within the base's limit!")
        total = (base * total) + int(number)

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

    finaltally = ""
    # Keep dividing number further and further
    # Each time, add the result to a final string of digits
    # Do this until there is no remainder
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            remainder = chr(LCASE_ASCII + remainder)
        finaltally = str(remainder) + finaltally
        number = number // base

    return finaltally



def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # I tried my best to go from one base directly to another
    # It didn't work. I'll just do this for now.
    return encode(decode(digits, base1), base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
