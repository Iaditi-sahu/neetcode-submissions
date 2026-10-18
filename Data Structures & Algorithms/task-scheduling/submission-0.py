from collections import Counter 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        m = count.most_common(1)[0][1]
        mCount = 0
        for _, c in count.items():
            if (c == m):
                mCount += 1
        prep = (m - 1) * (n + 1)
        suffix = mCount
        return max(prep+suffix, len(tasks))
