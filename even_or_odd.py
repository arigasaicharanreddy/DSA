class Solution :
    def Even_Odd(self, N : int) -> str:
        if N % 2 == 0:
            return "Even"
        else :
            return "Odd"
        
obj = Solution()
sol = obj.Even_Odd(45)
print(sol)