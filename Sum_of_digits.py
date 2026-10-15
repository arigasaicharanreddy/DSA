class Solution:
    def Sum_of_Digits(self, N : int) -> int:
        sum = 0
        num = abs(N)
        
        while num > 0 :
            digit = num % 10
            sum = sum + digit 
            num = num // 10
            
        return sum
    
obj = Solution()
sol = obj.Sum_of_Digits(564)
print(sol)
            
        