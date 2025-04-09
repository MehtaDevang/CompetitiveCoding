"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
 
Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)

        if n < m:
            return False
        if not t:
            if not s:
                return True
            return False
        if not s:
            return True
        
        left_t = 0
        left_s = 0

        while left_t < n:
            if t[left_t] == s[left_s]:
                left_s += 1
                if left_s == m:
                    return True
            left_t += 1
        return False
        