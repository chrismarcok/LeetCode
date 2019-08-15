class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aPlusIndex = a.index("+")
        bPlusIndex = b.index("+")
        a_iIndex = a.index("i")
        b_iIndex = b.index("i")
        a1, b1 = int(a[:aPlusIndex]), int(b[:bPlusIndex])
        a2, b2 = int(a[aPlusIndex + 1:a_iIndex]), int(b[bPlusIndex + 1:b_iIndex])
        
        A = a1 * b1 #main num
        Bi = (a1 * b2) + (a2 * b1) #num of i
        last = -(a2 * b2)
        
        
        return "{0}+{1}i".format(A + last, Bi)