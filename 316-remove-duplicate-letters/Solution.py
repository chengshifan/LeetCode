class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and stack[-1] in s[i + 1:]:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
