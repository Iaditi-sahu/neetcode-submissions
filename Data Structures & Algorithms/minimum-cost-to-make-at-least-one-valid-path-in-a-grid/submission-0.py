import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        # Distance matrix initialized to infinity
        costs = [[float('inf')] * cols for _ in range(rows)]
        costs[0][0] = 0

        # Priority Queue stores: (cost, r, c)
        pq = [(0, 0, 0)]

        while pq:
            cost, r, c = heapq.heappop(pq)
            
            # Standard Dijkstra's check: skip if we found a better path already
            if cost > costs[r][c]:
                continue
            
            # Target reached
            if r == rows - 1 and c == cols - 1:
                return cost
                
            # Check all 4 neighbors
            for i, (dr, dc) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)], 1):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Cost is 0 if grid matches the move direction, 1 otherwise
                    new_cost = cost + (0 if grid[r][c] == i else 1)
                    
                    if new_cost < costs[nr][nc]:
                        costs[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        
        return costs[rows-1][cols-1]