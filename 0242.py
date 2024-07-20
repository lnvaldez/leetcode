class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)

        if set_s != set_t:
            return False
        else:
            for char in set_s:
                s_count = s.count(char)
                t_count = t.count(char)

                if s_count != t_count:
                    return False 
            return True

