class Solution:
    def findComplement(self, num: int) -> int:
        b_num = list(f"{num:00b}")

        for i in range (len(b_num)):
            if b_num[i] == '1':
                b_num[i] = '0'
            else:
                b_num[i] = '1'
        
        comp = ''.join(b_num)
        return int(comp, 2)



s = Solution()
print(s.findComplement(num = 5))