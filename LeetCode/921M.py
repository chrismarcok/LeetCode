class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        num = 0
        for x in range(len(S)):
            if (S[x] == '('):
                stack.append(S[x])
            else:
                try:
                    stack.pop()
                except:
                    num += 1
        return num + len(stack)