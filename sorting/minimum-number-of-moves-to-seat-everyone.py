class Solution(object):
    def merge(self, arr, low, mid, high):
        n_left = mid - low + 1
        n_right = high - mid

        left_arr = [0] * n_left
        right_arr = [0] * n_right

        for i in range(n_left):
            left_arr[i] = arr[low+i]
        
        for j in range(n_right):
            right_arr[j] = arr[mid+j+1]
        
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
            k+=1
            i+=1
        
        while j < n_right:
            arr[k] = right_arr[j]
            k+=1
            j+=1

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        
        mid = low + (high-low) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid+1, high)
        self.merge(arr, low, mid, high)

    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        # sort both the arrays
        # seats = self.bubbleSort(seats)
        # students = self.bubbleSort(students)
        arr = seats
        self.mergeSort(arr, 0, len(seats)-1)
        seats = arr

        arr = students
        self.mergeSort(arr, 0, len(students)-1)
        students = arr

        minMoves = 0
        for i in range(len(seats)):
            ithMove = seats[i] - students[i]
            if ithMove < 0:
                ithMove *= -1
            minMoves += ithMove
        return minMoves