class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adjList = []
        result = []
        for i in range(n):
            adjList.append([])

        indegree = [0]*n
        
        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                result.append(i)
                q.append(i)
            
        
        while q:
            front = q.popleft()
            for x in adjList[front]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    result.append(x)
                    q.append(x)
        return len(result) == n