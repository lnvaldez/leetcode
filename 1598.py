class Solution:
    def minOperations(self, logs: List[str]) -> int:
        main = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if main > 0:
                    main -= 1
            elif logs[i] == "./":
                main = main 
            else:
                main += 1 
        return main
