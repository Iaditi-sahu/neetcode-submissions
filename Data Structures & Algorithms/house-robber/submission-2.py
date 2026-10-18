class Solution:
    def rec(self, i, nums, dp):
        if i>=len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        taken = nums[i] + self.rec(i+2, nums, dp)

        not_taken = self.rec(i+1,nums, dp)
        dp[i] = max(taken, not_taken)
        return dp[i]
    def rob(self,nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0],nums[1])
        for i in range(2, n):
            not_taken = b
            taken = nums[i] + a
            
            c = max(taken, not_taken)
            a = b
            b = c
        return b