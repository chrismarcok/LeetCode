class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        final_loc = -1
        for x in range(len(trips)):
            final_loc = max(final_loc, trips[x][2])
        
        for x in range(final_loc + 1):
            
            for y in range(len(trips)):
                
                if (trips[y][1] == x):
                    capacity -= trips[y][0]
                if (trips[y][2] == x):
                    capacity += trips[y][0]
            if (capacity < 0):
                    return False
        return True