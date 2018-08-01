class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lst = []

        for word in words:
            s = ""
            for ch in word:
                s += morse[ord(ch) - 97]
            lst.append(s)
        return len(set(lst))
