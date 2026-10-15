class Solution:
    def Grade_Calculator(self, n : int) -> str:
        if 90 <= n <= 100:
            return "A"
        elif 80 <= n <= 89:
            return "B"
        elif 70 <= n <= 79:
            return "C"
        elif 60 <= n <= 69:
            return "D"
        elif 50 <= n <= 59:
            return "E"
        elif 0 <= n <= 49:
            return "F"
        else : 
            return "Invalid Input"
        
obj = Solution()
sol = obj.Grade_Calculator(47)
print(sol)
        