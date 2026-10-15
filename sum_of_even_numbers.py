class Solution:
    def sumOfEvenNumbers(self, n: int) -> int:
        sum = 0
        
        for i in range (1, n + 1):
            if i % 2 == 0:
                sum = sum + i
                
        return sum
    
obj = Solution()
sol = obj.sumOfEvenNumbers(10)
print(sol)