
class Solution:
    def Largest_of_3_Integers(self, a: int, b: int, c: int) -> int:
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c

obj = Solution()
sol = obj.Largest_of_3_Integers(20, 20, 20)
print(sol)
