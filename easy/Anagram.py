# Question: https://leetcode.com/problems/valid-anagram/description/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false



def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = Counter(s)

    for i in t:
        if i in count and count[i]>0:
            count[i]-=1
        else:
            return False
    return True

    # Time Complexity: 𝚹(n)
    # Space Complexity: O(n)
    # if there are m distinct characters in string s then it will be 𝚹(m).
    # Best case scenario, there is only 1 distinct character or all characters are distinct.
   