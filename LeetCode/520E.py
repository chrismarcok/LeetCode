class Solution:
    def detectCapitalUse(self, s):
        """
        :type word: str
        :rtype: bool
        """
        if s.upper() == s:
            return True
        elif s.lower() == s:
            return True
        elif len(s) > 1 and s[0].upper() == s[0] and s[1:].lower() == s[1:]:
            return True
        return False
