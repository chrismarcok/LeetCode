class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lst = []
        largest = len(S)
        smallest = 0
        
        for x in range(len(S)):
            if S[x] == "D":
                lst.append(largest)
                largest -= 1
            else:
                lst.append(smallest)
                smallest += 1
        lst.append(smallest)
        return lst