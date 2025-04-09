"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n-1

        l_max = height[left]
        r_max = height[right]
        
        total_water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                l_max = max(l_max, height[left])
                total_water_trapped = total_water_trapped + (l_max - height[left])
                left += 1
            else:
                r_max = max(r_max, height[right])
                total_water_trapped = total_water_trapped + (r_max - height[right])
                right -= 1
        return total_water_trapped


        # BRUTE FORCE APPROACH - O(N)
        # left_max_arr = [0] * n
        # left_max = height[0]
        # for i in range(n):
        #     left_max = max(left_max, height[i])
        #     left_max_arr[i] = left_max
        
        # right_max_arr = [0] * n
        # right_max = height[n-1]
        # i = n-1
        # while i >= 0:
        #     right_max = max(right_max, height[i])
        #     right_max_arr[i] = right_max
        #     i -= 1
        
        # total_water_trapped = 0

        # for i in range(1, n-1):
        #     total_water_trapped = total_water_trapped + ((min(left_max_arr[i], right_max_arr[i]) - height[i]))
        
        # return total_water_trapped
