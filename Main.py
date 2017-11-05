def convert_from_10(number, target_base):
    """
    Convert number in target_base from base 10
    :param number: number you want to convert (int)
    :param target_base: target base of the number (int)
    :return: the converted number in target_base (str)

    Note
    ----
    target_base >= 2
    """

    quotient = []
    lefts = []
    result = ''

    while number != 0:
        quotient.append(number // target_base)
        lefts.append(number % target_base)
        number //= target_base

    for left in lefts:
        if left > 9:
            result = get_letter_from_index(left) + result
        else:
            result = str(left) + result

    return result


def get_letter_from_index(index):
    indexes = {
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
        15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
        20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
        25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
        30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y',
        35: 'Z'
    }

    if index in indexes:
        return indexes[index]
