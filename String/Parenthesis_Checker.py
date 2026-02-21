# Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
# An expression is balanced if:Each opening bracket has a corresponding closing bracket of the same type. Opening brackets must be closed in the correct order.


class Solution:
    def isBalanced(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # Opening bracket
            if ch in '([{':
                stack.append(ch)
            else:
                # Closing bracket
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
