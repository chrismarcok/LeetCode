class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == -b:
            return 0
        if a * b >= 0:
            a = "{0:b}".format(a)
            b = "{0:b}".format(b)
            neg = False
            if (int(a) < 0):
                a = a[1:]
                b = b[1:]
                neg = True
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
            if neg:
                return -int(res, 2)
            return int(res, 2)
        else:
            return sum([a, b])
            # idk how
