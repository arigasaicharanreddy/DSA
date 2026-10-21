class Solution:
    def Abs_without_builtin(self, n : int) -> int :
        if n < 0 :
            n = -(n)
            return n
        else :
            return 0
        
obj = Solution()
sol = obj.Abs_without_builtin(-9)
print(sol)
