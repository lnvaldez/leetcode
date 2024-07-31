from collections import Counter 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for k in counter.keys():
            if counter[k] == 1:
                return s.index(k)
        return -1
        