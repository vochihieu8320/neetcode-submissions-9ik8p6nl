class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            "{" : "}",
            "(": ")",
            "[" : "]"
        }

        stack = [s[0]]
        for i in range(1, len(s)):
            last_element = stack[len(stack) - 1] if len(stack) > 0 else None
            close_bracket = close_brackets.get(last_element, None)
            if close_bracket == s[i]:
                stack.pop()
            else:
                stack.append(s[i]) 

        return len(stack) == 0
        