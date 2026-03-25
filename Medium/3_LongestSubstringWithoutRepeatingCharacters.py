# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        p1 = 0
        p2 = 1
        length = len(s)
        result = 0
        seen = set()
        seen.add(s[p1])

        while p2<length:
            if s[p2] in seen:
                result = max(result, len(seen))
                prevp1 = p1
                p1 = p2-1
                while(s[p1] != s[p2]):
                    p1-=1
                for i in range(prevp1, p1+1):
                    seen.remove(s[i])
                p1+=1
            seen.add(s[p2])
            p2+=1
        return max(result, len(seen))
            
            
# Time complexity: O(n^2)
# Space complexity: O(n)