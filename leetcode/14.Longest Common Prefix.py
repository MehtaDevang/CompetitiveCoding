"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""

Explanation: There is no common prefix among the input strings.
 
Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            while s.find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix


"""
another solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if n == 1:
            return strs[0]

        shortest_string = strs[0]
        for i in range(1, n):
            if len(strs[i]) < len(shortest_string):
                shortest_string = strs[i]
        
        s_len = len(shortest_string)
        current_prefix = ""
        for i in range(s_len):
            current_prefix = current_prefix + shortest_string[i]
            for j in range(n):
                if not strs[j].startswith(current_prefix):
                    current_prefix = current_prefix[:-1]
                    return current_prefix
                else:
                    pass
        return current_prefix

"""