class Solution:
    def FizzBuzz(self, N : int) -> str :
        for i in range (1, N + 1) :
            if i  % 15 == 0:
                print("Fizz Buzz")
            elif i % 3 == 0  :
                print("FIZZ")
            elif i % 5 == 0:
                print("Buzz")
            else :
                print(str(i))
                
obj = Solution()
sol = obj.FizzBuzz(16)
print(sol)