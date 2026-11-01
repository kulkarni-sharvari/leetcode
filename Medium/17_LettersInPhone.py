# 17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

################################### Examples ###################################

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

################################### Solution ###################################

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtracking(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            for c in keys[digits[i]]:
                backtracking(i+1, currStr + c)
        
        if digits:
            backtracking(0,"")
        
        return res

################################## Complexity ##################################
