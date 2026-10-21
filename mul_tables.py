class Solution :
    def Mul_Tables(self, N : int) -> list[int] :
        
        table = []
        
        for i in range(1, 11):
            table.append(N * i)
            
        return table
    
obj = Solution()
sol = obj.Mul_Tables(5)
print(sol)
        