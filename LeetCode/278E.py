# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        end = n
        start = 1
        mid = 0
        d = {1: isBadVersion(1), n: isBadVersion(n)}
        this = False
        while (True):
        
            mid = (start + end) // 2
            
            if mid == 1 and d[1]:
                return 1
            elif mid == n:
                return n
            
            if mid not in d:
                this = isBadVersion(mid)
                d[mid] = this
            else:
                this = d[mid]
            
            if this:
                if (mid - 1) not in d:
                    d[mid - 1] = isBadVersion(mid - 1)
                if (d[mid - 1] == False):
                    return mid
                else:
                    end = mid - 1
            else:
                if (mid + 1) not in d:
                    d[mid + 1] = isBadVersion(mid + 1)
                if (d[mid + 1] == True):
                    return mid + 1
                else:
                    start = mid + 1