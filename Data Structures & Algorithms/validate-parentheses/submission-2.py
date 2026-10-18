class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = { ')':'(',  ']':'[', '}':"{" }
        for c in s:
            if c in dict:
                if stack and stack[-1] == dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False