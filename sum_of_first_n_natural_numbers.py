class Solution :
    def SumNNaturalNumbers(self, N : int) -> int :
        sum = 0
        for i in range(1, N + 1) :
            sum = sum + i
            
        return sum
    
obj = Solution()
sol = obj.SumNNaturalNumbers(5)
print(sol)