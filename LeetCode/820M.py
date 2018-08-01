# solution is valid but times out

class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst = []
        res = ""
        words.sort(key=len, reverse=True)
        for x in range(len(words)):
            if self.shouldDiscardWord(words[x], lst):
                continue
            else:
                lst.append(words[x])
                res += words[x] + "#"

        return len(res)

    def shouldDiscardWord(self, word, lst):
        for x in lst:
            if word == x[-len(word):]:
                return True
        return False

# other solution
class Solution(object):
    def minimumLengthEncoding(self, words):
        s = set(words)
        for word in words:
            for x in range(1, len(word)):
                s.discard(word[x:])
        return len(s) + sum([len(x) for x in s])
