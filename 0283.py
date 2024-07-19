class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:
                nums.append(nums.pop(nums.index(i)))
        print(nums)
