class Solution :
    def Sign_OF_Integer(self, n : int) -> str :
        if n < 0 :
            return "Negative"
        elif n == 0: 
            return "Zero"
        else:
            return "Positive"
        
obj = Solution()
sol = obj.Sign_OF_Integer(-4)
print(sol)