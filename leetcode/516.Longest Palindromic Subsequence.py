"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:
    1 <= s.length <= 1000
    s consists only of lowercase English letters.
"""
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l,r=0,len(s)-1
        cache = {}
        def largest_palindrome(l,r):
            if (l,r) in cache:
                return cache[(l,r)]
            if r < l:
                return 0
            if l==r:
                return 1
            max_len=0
            if s[l]==s[r]:
                max_len= 2 + largest_palindrome(l+1 , r-1)
            else:
                max_len += max(largest_palindrome(l+1 , r) , largest_palindrome(l ,r-1))
            cache[(l,r)] = max_len
            return cache[(l,r)]
        return largest_palindrome(l,r)
        