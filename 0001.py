class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        n = len(nums)

        for i in range(n):
            for j in range(n - 1):
                if i != j + 1:
                    if nums[i] + nums[j + 1] == target:
                        index.append(i)
                        index.append(j + 1)
                        return index

