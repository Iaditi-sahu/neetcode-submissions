class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed: int)-> bool:
            return sum(math.ceil(p/speed) for p in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left 