# 784 Letter case permutation - https://leetcode.com/problems/letter-case-permutation/description/
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

################################### Examples ###################################

# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]

################################### Solution ###################################

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []
        n = len(s)
        s = s.lower()

        def backtracking(i, local):
            if i==n:
                res.append("". join(local))
                return
            
            if s[i].isalpha():
                local.append(s[i].upper())
                backtracking(i+1, local)
                local.pop()
                local.append(s[i])
                backtracking(i+1, local)
                local.pop()

            else:
                local.append(s[i])
                backtracking(i+1, local)
                local.pop()

        backtracking(0,[])
        return res