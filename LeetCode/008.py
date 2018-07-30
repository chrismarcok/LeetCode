def myAtoi(str):
    """
    >>> myAtoi("42")
    42
    >>> myAtoi("    -42")
    -42
    >>> myAtoi("321 with words")
    321
    >>> myAtoi("dsa 31")
    0
    >>> myAtoi("-32154325431432143")
    -2147483648
    >>> myAtoi("-")
    0
    >>> myAtoi("321321-")
    321321
    >>> myAtoi("-3213-")
    -3213
    >>> myAtoi('-+1')
    0
    >>> myAtoi("+1")
    1
    >>> myAtoi("+-2")
    0
    >>> myAtoi("+32132 gfdsg")
    32132
    >>> myAtoi("-5-")
    -5
    """

    INT_MIN = -2147483648
    INT_MAX = 2147483647
    str = str.strip(" ")
    if str == "" or str == "-" or str == "+":
        return 0

    if not str[0].isnumeric() and str[0] is not '-' and str[0] is not '+':
        return 0

    index = len(str)
    for x in range(len(str)):
        if (str[x].isnumeric() or (str[x] == '-' and x == 0) or (str[x] == '+' and x == 0)):
            continue
        else:
            index = x
            break
    str = str[:index]
    if str == '-' or str == '+':
        return 0
    num = int(str)
    if num < INT_MIN:
        return INT_MIN
    elif num > INT_MAX:
        return INT_MAX

    return num

