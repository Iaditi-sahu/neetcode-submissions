class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        c1, c2 = 0, 0
        cnd1, cnd2 = None, None
        for num in nums:
            if num == cnd1:
                c1 += 1
            elif num == cnd2:
                c2 += 1
            elif c1 == 0:
                cnd1 = num
                c1 = 1
            elif c2 == 0:
                cnd2 = num
                c2 == 1
            else:
                c1 -= 1
                c2 -= 1

        result = []
        threshold = len(nums)//3

        c1, c2 = 0, 0
        for num in nums:
            if num == cnd1:
                c1 += 1
            elif num == cnd2:
                c2 += 1
        
        if c1 > threshold:
            result.append(cnd1)
        if c2 > threshold:
            result.append(cnd2)

        return result
