# N = 28  , FACT = 1,2,4,7,14  SUM = 1+2+4+7+14 = 28

class Solution :
    def perfect_number(self, a : int) -> bool :
        sum = 0 
        original = a
        
        for i in range (1, a) :
            if a % i == 0 :
                sum = sum + i
                
        return sum == original
    
obj = Solution()
sol = obj.perfect_number(48)
print(sol)
