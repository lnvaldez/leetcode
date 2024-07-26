from collections import Counter 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m_1 = []
        m_2 = []

        for char in s:
            m_1.append(s.index(char))
        for char in t:
            m_2.append(t.index(char))

        if m_1 == m_2:
            return True
        else:
            return False 

s = Solution()
print(s.isIsomorphic("bbbaaaba", "aaabbbba"))