class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        if strs == []:
            return s
        for x in range(len(min(strs, key=len))):
            if len(set(self.getLetters(strs, x))) == 1:
                s += strs[0][x]
            else:
                break
        return s
            
            
    def getLetters(self, lst, index):
        list_ = []
        for x in lst:
            list_.append(x[index])
        return list_