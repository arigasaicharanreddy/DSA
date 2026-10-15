class Solution:
    def Voting_Eligibility(self, n : int) :
        if n >= 18:
            return True
        else:
            return False
        
sol = Solution().Voting_Eligibility(43)
print(sol)
