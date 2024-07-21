from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        top_k = [item for item, count in freq.most_common(k)]

        return top_k


