class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            n = nums[i]
            r = target - n

            if r not in temp:
                temp[n] = i
            else:
                return [temp[r], i]