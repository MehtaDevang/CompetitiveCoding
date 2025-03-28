"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        # store the last seen index of the characters
        character_index = {}

        i = 0

        # iterating over the complete set
        longest_substring_length = 1
        current_length = 0
        while i < n:
            if s[i] not in character_index:
                character_index[s[i]] = i
                current_length += 1
                if current_length > longest_substring_length:
                    longest_substring_length = current_length
                i+=1
                
            else:
                last_seen_index_of_current_character = character_index[s[i]]
                i = last_seen_index_of_current_character + 1
                current_length = 0
                character_index = {}
        return longest_substring_length
