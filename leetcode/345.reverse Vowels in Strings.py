"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation:
        The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)

        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        
        left = 0
        right = n - 1
        left_vowel = None
        right_vowel = None
        s = list(s)
 
        while left < right:
            if s[left] in vowels:
                left_vowel = left
            else:
                left += 1

            if s[right] in vowels:
                right_vowel = right
            else:
                right -= 1
            
            if right_vowel is not None and left_vowel is not None:
                s[right_vowel], s[left_vowel] = s[left_vowel], s[right_vowel]
                left_vowel = None
                right_vowel = None

                left += 1
                right -= 1
        return "".join(s)

