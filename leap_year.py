class Solution :
    def Leap_Year(self, n : int) -> bool:
        if n % 4 == 0 or (n % 400 == 0 and n % 100 != 0):
            return True
        else:
            return False
        
obj = Solution()
sol = obj.Leap_Year(2024)
print(sol)