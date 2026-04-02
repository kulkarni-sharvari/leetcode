# 125. Valid Palindrome https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char)
        string = "".join(chars)
        
        p1 = 0
        p2 = len(string)-1
        while p1<=p2:
            if string[p1] != string[p2]:
                return False
            p1+=1
            p2-=1
        return True

# Time Complexity: ϴ(n)
# Traverse through every character to check if it is alphanumeric = ϴ(n)
# Treverse through 2 characters at every loop = ϴ(n/2) = ϴ(n)
# Total TC = ϴ(n) + ϴ(n) = ϴ(n)

# Space Complexity: O(n)
# a new string is generated to keep all the alphanumeric characters of s. In woirst case, it will be O(n)
