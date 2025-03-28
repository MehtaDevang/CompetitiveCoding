"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.
 

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""

class Solution(object):
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = False
            if not swapped:
                break
        return arr

    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
    
    def merge(self, arr, low, mid, high):
        n_left = mid - low + 1
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
            if left_arr[i] <= right_arr[j]:
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
        
    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        
        mid = low + (high-low) // 2

        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid+1, high)
        self.merge(arr, low, mid, high)

    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """

        # self.mergeSort(nums, 0, len(nums)-1)
        nums.sort()
        result = []

        for query in queries:
            count = 0
            i = 0

            while query >= 0 and i < len(nums):
                if query < nums[i]:
                    result.append(count)
                    break
                else:
                    count+=1
                    query = query-nums[i]
                i+=1
            if i >= len(nums):
                result.append(len(nums))
        return result

        