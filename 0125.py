import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s) 
        s = s.lower()

        rev_s = s[::-1]

        if s == rev_s:
            return True 
        else:
            return False