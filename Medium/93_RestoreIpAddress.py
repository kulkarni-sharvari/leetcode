# 93. Restore IP restoreIpAddresses - https://leetcode.com/problems/restore-ip-addresses/description/

# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

################################### Examples ###################################

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

################################### Solution ###################################

class Solution:

    def isValid(self, val):
        intVal = int(val)

        if (intVal< 0 or intVal>255 or (len(val)>1 and val[0]=='0')):
            return False
        return True

    def restoreIpAddresses(self, s: str) -> list[str]:
        res = list()
        n = len(s)

        if n>12 or n<4:
            return []
        
        def backtracking(i, dots, currIP):
            # base condition
            if i==n and dots==4:
                res.append(currIP[:-1])
                return
            if dots>=4 or i == n:
                return

            for j in range(i,min(i + 3, n)):
                if self.isValid(s[i:j+1]):
                    backtracking(j+1, dots+1, currIP+s[i:j+1]+".")
        
        backtracking(0,0,"")
        return res
