class Solution : 
    def reverseString(self, s : str) -> str :
        rev = s[::-1]
        return rev
    
obj = Solution()
sol = obj.reverseString("hello")
print(sol)
