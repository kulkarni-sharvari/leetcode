# https://leetcode.com/problems/minimum-window-substring/description/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        p1 = 0
        p2 = 0
        result = ""
        resultLen = len(s)

        freqNeed = {}
        for char in t:
            freqNeed[char] = freqNeed.get(char, 0) + 1

        freqHave = {}
        i=0
        while i<= p2 and i<len(s):
            freqHave[s[i]] = freqHave.get(s[i], 0) + 1
            i+=1
        
        while p1 <= p2 and p2 < len(s):
            allFound = True
            for key in freqNeed:
                if freqHave.get(key, 0) < freqNeed[key]:
                    allFound = False
                    break
            if allFound:
                if resultLen >= p2 - p1 + 1:
                    result = s[p1:p2+1]
                    resultLen = p2 - p1 + 1
                if freqHave.get(s[p1], 0) > 0:
                    freqHave[s[p1]] -= 1
                p1 += 1

            else:
                p2 += 1
                if p2<len(s):
                    if freqNeed.get(s[p2], 0) > 0:
                        freqHave[s[p2]] = freqHave.get(s[p2], 0) + 1

        return result

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
result = solution.minWindow(s, t)
print(result)


# Time complexity analysis: O(len(s)*unique characters of t)
#  worst case - all characters are unique in t. 
# Therefore timecomplexity = O(len(s)*len(t))

# Space complexity: O(k) where k denotes the number of unique characters in t.