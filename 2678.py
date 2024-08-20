class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                c += 1
        return c

