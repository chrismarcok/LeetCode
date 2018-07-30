def longestPalindrome(s):
    """
    >>> longestPalindrome("abad")
    'aba'
    >>> longestPalindrome("abbd")
    'bb'
    >>> longestPalindrome("")
    ''
    >>> longestPalindrome("a")
    'a'
    """
    n = len(s)
    if n == 1 or n == 0 or isPalindrome(s):
        return s
    word = ""
    biggest = 0
    for x in range(n):
        if (x + biggest > n):
            break
        for y in range(n, x, -1):
            # print(y - x)
            if (y - x < biggest):
                break
            substr = s[x:y]
            # print(substr)
            if len(substr) > biggest and isPalindrome(substr):
                biggest = len(substr)
                word = substr
    return word


def isPalindrome(s):
    """
    >>> isPalindrome("aba")
    True
    >>> isPalindrome("")
    True
    >>> isPalindrome("a")
    True
    >>> isPalindrome("abc")
    False
    >>> isPalindrome("aa")
    True
    >>> isPalindrome("ab")
    False
    """
    return s == s[::-1]