class Solution:
    def countAndSay(self, n: int) -> str:
        d = {}
        d[1] = "1"
        d[2] = "11"
        d[3] = "21"
        d[4] = "1211"
        d[5] = "111221"
        for x in range(6, n + 1):
            s = ""
            
            num = d[x-1]
            
            y = 0
            while (y < len(num)):
                curNum = num[y]
                numOfCurNum = self.countSame(num, y)
                s += str(numOfCurNum) + curNum
                y += numOfCurNum
                                
            d[x] = s
        return d[n]
            
    def countSame(self, s, i) -> int:
        num = s[i]
        count = 0
        for x in range(i, len(s)):
            if num == s[x]:
                count += 1
            else:
                break
        return count