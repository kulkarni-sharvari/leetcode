# 131. Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/description/
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 
################################### Examples ###################################

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

################################### Solution ###################################

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        sol, local = [], []
        n = len(s)

        def backtracking(i):
            if i>=n:
                sol.append(local.copy())
                return
            
            for j in range(i,n):
                if self.isPalindrome(s, i, j):
                    local.append(s[i:j+1])
                    backtracking(j+1) # backtracking on the remaining characters.
                    local.pop()
                
                

        backtracking(0)
        return sol

    def isPalindrome(self, s: str, l: int, r: int):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r = l+1, r-1
        return True
    