# str = "arigasaicharanreddy" = a,i,a,a,i,a,a,e = 8

class Solution :
    def vowels(self, a : str) -> int :
        count = 0
        
        for char in a : 
            if char in "aeiouAEIOU" :
                count += 1 
        return count


obj = Solution()
sol = obj.vowels("arigaSAICHARANreddy")
print(sol)
