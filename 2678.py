from typing import List 

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                c += 1
        return c

s = Solution()
print(s.countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"]))