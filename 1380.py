class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []

        m = len(matrix)
        n = len(matrix[0])

        col = []

        min_list = [min(row) for row in matrix]

        max_list = []
        for j in range(n):
            col = [matrix[i][j] for i in range(m)]
            max_list.append(max(col))

        for x in min_list:
            if x in max_list:
                lucky_nums.append(x)

        return lucky_nums
                

