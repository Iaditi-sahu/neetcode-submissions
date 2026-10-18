class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r, c = len(matrix), len(matrix[0])
        left, right = 0, (r * c) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // c][mid % c]

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
