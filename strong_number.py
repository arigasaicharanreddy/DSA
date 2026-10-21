class Solution :
    def Strong_Number(self, n : int) -> bool :
        N = n
        sum = 0
        
        while n > 0 :
            digit = n % 10
            fact = 1
            for i in range(1, digit + 1):
                fact = fact * i
            sum = sum + fact
                
            n = n // 10
                
        return sum == N
    
obj = Solution()
sol = obj.Strong_Number(145)
print(sol)
                