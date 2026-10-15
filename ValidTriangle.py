class Solution:
    def Triangle(self, a : int, b : int, c : int):
        if a + b > c and b + c > a and a + c > b:
            return True
        
obj = Solution()
sol = obj.Triangle(4,5,6)
print(sol)