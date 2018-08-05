class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        while len(a) != len(b):
            if len(a) < len(b):
                a = "0{}".format(a)
            else:
                b = "0{}".format(b)
        res = ""
        carry = 0
        for x in range(len(a)-1, -1, -1):
            if a[x] == "1" and b[x] == "1":
                res = "{}{}".format(str(carry), res)
                carry = 1
            elif a[x] != b[x]:
                if carry != 0:
                    res = "0{}".format(res)
                else:
                    res = "1{}".format(res)
            else:
                if carry != 0:
                    res = "1{}".format(res)
                    carry = 0
                else:
                    res = "0{}".format(res)
        if carry != 0:
            res = "1" + res
        return res
            