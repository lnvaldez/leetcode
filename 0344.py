from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        print(s)
        j = len(s) - 1
        for i in range(0, int(len(s) / 2)):
            t = s[i]
            s[i] = s[j]
            s[j] = t
            j -= 1
  