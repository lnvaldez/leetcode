class Solution():
    def maxProductDifference(self, nums: List[int]) -> int:
        l = []
        for i in range(4):
            if i < 2:
                l.append(max(nums)) 
                nums.remove(max(nums))
            else:
                l.append(min(nums)) 
                nums.remove(min(nums))
        return ((l[0] * l[1]) - (l[2] * l[3]))

