from typing import List 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left == right:
                return i
        return -1 
    
s = Solution()
print(s.pivotIndex(nums = [1,2,3]))