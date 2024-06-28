"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""

class Solution(object):
    def merge(self, arr, low, mid, high):
        n_left = mid-low+1
        n_right = high-mid

        left_arr = [[]] * n_left
        right_arr = [[]] * n_right
    
        for i in range(n_left):
            left_arr[i] = arr[low+i]
        
        for j in range(n_right):
            right_arr[j] = arr[mid+1+j]
        
        i = 0
        j = 0
        k = low

        while i < n_left and j < n_right:
            if sum(left_arr[i][:-1]) <= sum(right_arr[j][:-1]):
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

    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        for index, element in enumerate(mat):
            element.append(index)
        self.mergeSort(mat, 0, len(mat)-1)
        return [mat[i][-1] for i in range(k)] 