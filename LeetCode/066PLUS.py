class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [9]:
            return [1,0]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            carry = 0
            for x in range(len(digits) - 1, -1, -1):
                if x == len(digits) - 1 and digits[x] == 9:
                    digits[x] = 0
                    carry = 1
                    continue
                else:
                    digits[x] += carry
                    if digits[x] == 10:
                        carry += 1
                    digits[x] %= 10
                    if carry > 0:
                        carry -= 1
            if carry > 0:
                s = [1]
                s.extend(digits)
                digits = s
        return digits

# SOLUTION TWO

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for x in range(len(digits)):
            s += str(digits[x])
        s = int(s)
        s += 1

        s = str(s)

        res = []
        for ch in s:
            res.append(int(ch))
        return res