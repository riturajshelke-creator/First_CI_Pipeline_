def is_anagram(first, second):
    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")

    if len(first) != len(second):
        return False

    char_count = {}

    for char in first:
        char_count[char] = char_count.get(char, 0) + 1

    for char in second:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True