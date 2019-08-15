from operator import itemgetter

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(people)
        result = [None for x in range(length)]
        inserts = 0
        
        while inserts < length:
            
            minNum = self.getMin(people)
            minLst = [x for x in people if x[0] == minNum]
            people = [x for x in people if x[0] != minNum]
            
            minLst.sort(key = lambda x: x[1]) 
            
            while len(minLst) != 0:
                lst = minLst[-1]
                noneSeen = 0
                for x in range(length):
                    if result[x] is None:
                        noneSeen += 1
                    if noneSeen - 1 == lst[1]:
                        result[x] = lst
                        inserts += 1
                        break
                minLst.pop()
                
           
        
        return result
        
    def getMin(self, people):
        m = float("inf")
        
        for x in range(len(people)):
            if people[x][0] < m:
                m = people[x][0]
        return m