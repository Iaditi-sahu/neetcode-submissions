class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            a, b = 0, 0

            for i in nums:
                c = max(a + i, b)
                a = b
                b = c
            return b
        return max(helper(nums[1:]), helper(nums[:-1]))