class Solution :
    def lcm(self, a : int, b : int) -> int :
        x, y = a, b
        
        while y != 0 :
            x,y = y, x%y 
            
        gcd = x 
        
        return (a * b) // gcd
    
obj = Solution()
sol = obj.lcm(5,6)
print(sol)