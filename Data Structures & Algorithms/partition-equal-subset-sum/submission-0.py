class Solution:
    
    def rec(self, i, sum1, nums, total, dp):
        if sum1 == (total // 2):
            return True
        elif sum1 >= (total//2) or i == len(nums):
            return False
         
        
        if dp[i][sum1] != -1:
            return dp[i][sum1]

        taken = self.rec(i+1, sum1+nums[i], nums, total, dp) 
        not_taken = self.rec(i+1, sum1, nums, total, dp) 

        dp[i][sum1] = taken or not_taken
        return dp[i][sum1]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        
        total = sum(nums)

        if total % 2 == 1:
            return False
        dp = [[-1 for j in range((total//2)+1)] for i in range(n)]

        return self.rec(0, 0, nums, total, dp)