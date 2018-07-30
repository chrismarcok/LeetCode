class Solution:
    def hammingDistance(self, x, y):
        """
        >>> hammingDistance(1,4)
        2
        """
        count = 0
        str1 = self.convertIntToBinaryStr(x)
        str2 = self.convertIntToBinaryStr(y)

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

    def convertIntToBinaryStr(self, num):
        """
        >>> convertIntToBinaryStr(1)
        '00000000000000000000000000000001'
        >>> convertIntToBinaryStr(4)
        '00000000000000000000000000000100'
        """
        result = ""
        pow = 31

        while (num > 0):

            if num - (2 ** pow) < 0:
                pow = pow -1
                result = result + "0"
            else:
                num = num - 2 ** pow
                pow = pow - 1
                result = result + "1"

        while(len(result) != len("00000000000000000000000000000100")):
            result += "0"

        return result