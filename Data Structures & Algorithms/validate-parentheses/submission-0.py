class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackset = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in stackset:
                if stack and stack[-1] == stackset[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False        