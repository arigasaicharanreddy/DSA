class Solution :
    def Factorial(self, n:int) -> int :
        fact = 1
        i = 1
        
        for i in range (1, n + 1) :
            fact = fact * i
            
        return fact
    
obj = Solution()
sol = obj.Factorial(5)
print(sol)