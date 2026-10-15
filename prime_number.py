
class Solution:
    def Prime_Number(self, n: int) -> bool:
        count = 0

        if n < 2:
            return False

        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1

        return count == 2


obj = Solution()
sol = obj.Prime_Number(67)
print(sol)

