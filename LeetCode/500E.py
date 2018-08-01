class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        up = "qwertyuiopQWERTYUYIOP"
        mid = "asdfghjklASDFGHJKL"
        bot = 'zxcvbnmZXCVBNM'
        lst = []
        for word in words:

            add = True
            u,m,b = False, False, False
            if word[0] in up:
                u = True
            elif word[0] in mid:
                m = True
            else:
                b = True

            for ch in word:

                if u and ch not in up:
                    add = False
                    break
                elif m and ch not in mid:
                    add = False
                    break
                elif b and ch not in bot:
                    add = False
                    break
            if add:
                lst.append(word)

        return lst
