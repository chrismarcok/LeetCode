class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = []
        for email in emails:
            string = self.formatEmail(email)
            d.append(string)
        return len(set(d))
    
    def formatEmail(self, email):
        result = ""
        atIndex = email.index("@")
        for x in range(len(email)):
            if x == atIndex or email[x] == "+":
                break
            elif (email[x] != "."):
                result += email[x]        
        
        result += email[atIndex:]
        return result