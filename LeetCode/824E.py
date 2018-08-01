class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        lst = S.split(" ")
        result = ''

        for x in range(len(lst)):
            if lst[x][0] in "aeiouAEIOU":
                result += lst[x] + "ma" + ((x + 1) * "a" + "")
            else:
                result += (lst[x][1:] + lst[x][0] + "ma" + ((x + 1) * "a"))
            result += " "

        result = result.strip()
        return result
