class Solution:
    def power(self, a: int, b: int) -> int:
        result = 1

        while b > 0:
            if b % 2 == 1:
                result *= a

            a *= a
            b //= 2

        return result


obj = Solution()
sol = obj.power(5, 6)
print(sol)