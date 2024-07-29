class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst_p = []
        lst_s = []

        s = s.split(' ')

        for char in pattern:
            lst_p.append(pattern.index(char))
        for char in s:
            lst_s.append(s.index(char))

        if lst_p == lst_s:
            return True
        else:
            return False

s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))