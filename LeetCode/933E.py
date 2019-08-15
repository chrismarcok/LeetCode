import time
class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.pings.append(t)
        count = 0
        for x in self.pings:
            if x >= t - 3000:
                break
            count += 1
        self.pings = self.pings[count:]
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)