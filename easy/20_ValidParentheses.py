# 20. Valid Parentheses https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        stack = list()

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if c == ")" or c == "}" or c == "]":
                    if len(stack) <= 0:
                        return False
                    else:
                        popped = stack.pop()
                        if (c == ")" and popped != "(") or (c == "}" and popped != "{") or (c == "]" and popped != "["):
                            return False
        return len(stack) == 0

# Time complexity: 𝚹(n)
# Space Complexity: O(n)