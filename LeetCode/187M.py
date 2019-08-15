class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        res = []
        
        for x in range(len(s) - 9):
            string = s[x: x+10]
            if string not in d:
                d[string] = 0
            d[string] += 1
        for key in d:
            if d[key] > 1:
                res.append(key)
        return res