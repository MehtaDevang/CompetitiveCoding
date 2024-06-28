"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""

class Solution(object):
    def customSort(self, arr, indexMapper):
        n = len(arr)

        # implementing bubble sort
        for i in range(n):
            swapped = False
            for j in range(n-1-i):
                index_next = indexMapper.get(arr[j+1])
                index_current = indexMapper.get(arr[j])

                # both are in mapper
                if index_current > index_next:
                    # swap arr[j] and arr[j+1]
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    swapped = True
            if not swapped:
                break
        return arr


    def merge(self, arr, low, mid, high):
        n_left = mid-low+1
        n_right = high - mid

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
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        indexMapper = {}

        # creating a hashmap of elements to index of arr2
        for i in range(len(arr2)):
            indexMapper[arr2[i]] = i
        
        elements_not_in_arr2 = [x for x in arr1 if x not in indexMapper.keys()]
        elements_in_arr2 = [x for x in arr1 if x in indexMapper.keys()]

        elements_in_arr2 = self.customSort(elements_in_arr2, indexMapper)
        # self.mergeSort(elements_not_in_arr2, 0, len(elements_not_in_arr2)-1)
        elements_not_in_arr2 = sorted(elements_not_in_arr2)
        return elements_in_arr2+elements_not_in_arr2
        
        