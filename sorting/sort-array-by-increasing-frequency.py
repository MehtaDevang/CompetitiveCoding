"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

class Solution(object):

    def customSort(self, arr, mapper):
        # implementing bubble sort
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in  range(n-1-i):
                el1 = arr[j]
                el2 = arr[j+1]

                f1, f2 = mapper[el1], mapper[el2]
                if f1 > f2:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                elif f1 == f2 and arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr


    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        frequencyMapper = {}

        for element in nums:
            if element not in frequencyMapper:
                frequencyMapper[element] = 1
            else:
                frequencyMapper[element] += 1
        
        nums = self.customSort(nums, frequencyMapper)
        return nums
        