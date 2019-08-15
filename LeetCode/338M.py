class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = [0]
        for x in range(1, num + 1):
            if x % 2 == 1:
                lst.append(lst[x - 1] + 1)
            else:
                s = "0" + bin(x - 1)[2:]             
                count = 0
                for y in range(len(s) - 1, -1, -1):
                    if s[y] == "0":
                        break
                    else:
                        count += 1
                lst.append(lst[x-1] - count + 1)
                        
        return lst
                