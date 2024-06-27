# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

 

# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.
# Example 2:

# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
# Example 3:

# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# Explanation: There is no a single valid k, we return -1.
 

# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# nums[i] != 0

class Solution(object):
    def merge(self, arr, low, mid, high):
        n_left = mid-low+1
        n_right = high-mid

        left_arr = [0] * n_left
        right_arr = [0] * n_right

        for i in range(n_left):
            left_arr[i] = arr[low+i]

        for j in range(n_right):
            right_arr[j] = arr[mid+1+j]

        i = 0
        j = 0
        k = low

        while i < n_left and j < n_right:
            if abs(left_arr[i]) <= abs(right_arr[j]):
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        while i < n_left:
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < n_right:
            arr[k] = right_arr[j]
            j+=1
            k+=1
        
    def mergeSort(self, nums, low, high):
        if low >= high:
            return

        mid = low + (high-low) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def findMaxK(self, nums): 
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # self.mergeSort(nums, 0, n-1)
        nums.sort(key=abs)
        largest = 0
        for i in range(1, n):
            if nums[i] + nums[i-1] == 0:
                if abs(nums[i]) > largest:
                    largest = abs(nums[i])

        return largest if largest else -1
        