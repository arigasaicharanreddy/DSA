class Solution:
    def Electricity_bill(self, units : int) -> int :
        
        rate_1 = 5
        rate_2 = 7
        rate_3 = 10
        
        if 0 <= units <= 100 :
            bill = units * rate_1
        
        elif 101 <= units <= 300 :
            bill = (100 * rate_1) + ((units - 100) * rate_2)
        elif units > 300 :
            bill = (100 * rate_1) + (200 * rate_2) + ((units - 300) * rate_3)
            
        else: 
            bill = 0
            
        return bill
    
obj = Solution()
sol = obj.Electricity_bill(500)
print(sol)
        