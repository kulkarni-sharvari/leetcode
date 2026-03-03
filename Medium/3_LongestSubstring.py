# Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

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
        if len(s.strip()) == 0 and len(s)>0: 
            return 1
        left = 0
        right = 0
        unique = set()
        maxLength = 0
        while right < len(s):
            if s[right] in unique:
                unique.remove(s[left])
                left +=1
            else:
                unique.add(s[right])
                right +=1
            maxLength = max(maxLength, (right - left))
        
        return maxLength

sol = Solution()
eg1 = sol.lengthOfLongestSubstring("abcabcbb")
print(eg1)

eg2 = sol.lengthOfLongestSubstring("bbbbb")
print(eg2)

eg3 = sol.lengthOfLongestSubstring("pwwkew")
print(eg3)

# Time Complexity:𝚹(n)
# Space Complexity: O(n)
# Constant for right, left and maxLength.
# unique = O(n). 
