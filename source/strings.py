#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) == 0:
        return True

    pattern = list(pattern)
    p_len = len(pattern)

    clean_text = list(filter(str.isalnum, text))
    t_len = len(clean_text)

    for i in range(t_len):
        # If the first letter matches, check the rest of string
        if clean_text[i] == pattern[0]:
            # Go through each bit of pattern to make sure each matches
            for j in range(p_len):
                if i+j > t_len-1:
                    return False
                if pattern[j] != clean_text[i+j]:
                    break
                if j == p_len-1:
                    return True

    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Check if empty; if so, return 0, earliest bit
    if len(pattern) == 0:
        return 0

    pattern = list(pattern)
    p_len = len(pattern)

    text = list(text)
    t_len = len(text)

    shift = 0
    # Alternate way I read about: Boyer-Moore
    # Making sure that shift doesn't go past point of no return
    # You can't find 'def' in 'abcd' if you're already past b
    while(shift <= t_len - p_len):
        # We can only do it to the length of pattern
        index = p_len - 1
        # Keep going until it all meets
        while index >= 0 and pattern[index] == text[shift+index]:
            index -= 1
        # If we get past index, then return where the shift is
        if index < 0:
            return shift
        else:
            if text[shift+p_len-1] in pattern:
                shift += p_len - pattern.index(text[shift+p_len-1]) - 1
            else:
                shift += p_len
    # ALTERNATE SOLUTION - if you care about ignoring periods/don't like
    #
    # for i in range(t_len):
    #     # If the first letter matches, check the rest of string
    #     # Worst case O(n) + size of pattern; best case, size of pattern
    #     if text[i] == pattern[0]:
    #         foundindex = i
    #         skip = 0
    #         # Gradually goes through pattern by index
    #         for j in range(p_len):
    #             if i+j+skip > t_len-1:
    #                 return None
    #             while not text[i+j+skip].isalnum():
    #                 skip += 1
    #             if pattern[j] != text[i+j+skip]:
    #                 break
    #             if j == p_len-1:
    #                 return foundindex
    return None



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # If it's empty space, guess we're printing the entire thing
    # O(n)
    if pattern == '':
        foundindeces = []
        for i in range(len(text)):
            foundindeces.append(i)
        return foundindeces

    pattern = list(pattern)
    p_len = len(pattern)

    text = list(text)
    t_len = len(text)

    foundindeces = []

    shift = 0
    # Alternate way I read about: Boyer-Moore
    # Making sure that shift doesn't go past point of no return
    # You can't find 'def' in 'abcd' if you're already past b
    while(shift <= t_len - p_len):
        print("Loop start!", text[shift:])

        # We can only do it to the length of pattern
        index = p_len - 1
        # Keep going until it all meets
        while index >= 0 and pattern[index] == text[shift+index]:
            index -= 1
        # If we get past index, then shift up a bit and append to list
        if index < 0:
            foundindeces.append(shift)
            shift += 1
        else:
            # Otherwise, if it's in the pattern, move pattern to match
            if text[shift+p_len-1] in pattern:
                shift += p_len - pattern.index(text[shift+p_len-1]) - 1
            # Otherwise, shift as far as the length
            else:
                shift += p_len

    # Alternate; works with non alphanum
    # for i in range(t_len):
    #     # If the first letter matches, check the rest of string
    #     # Worst: O(n^2 if it's always matching)
    #     # Best: O(n) where nothing matches
    #     if text[i] == pattern[0]:
    #         foundindex = i
    #         skip = 0
    #         # Loop for going through pattern as a list
    #         for j in range(p_len):
    #             # Too far into text; stop right there
    #             if i+j+skip > t_len-1:
    #                 break
    #             # If it's not alphanumeric, skip to the next element
    #             while not text[i+j+skip].isalnum():
    #                 skip += 1
    #             # If that element doesn't match, it's not a full match
    #             if pattern[j] != text[i+j+skip]:
    #                 break
    #             # Found if go through all of pattern; append to list
    #             if j == p_len-1:
    #                 foundindeces.append(foundindex)
    #
    return foundindeces


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    if found:
        print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
        index = find_index(text, pattern)
        print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
        indexes = find_all_indexes(text, pattern)
        print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))

    else:
        print("String not found!")


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
