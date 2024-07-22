class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[i] = heights[i]
        keys = sorted(d, key = d.get)
        r = [names[k] for k in keys]
        return r[::-1]
