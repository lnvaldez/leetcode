class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        i = 0

        while i < len(nums):
            if nums[i] in s:
                del nums[i]
            else:
                s.add(nums[i])
                i += 1

        k = len(nums)
        return k
    
