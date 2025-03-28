"""
Bubble Sort
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arr[j] >= arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
        if not swapped:
            break
    return arr


"""
    Merge Sort
"""

def merge(arr, low, mid, high):
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


def mergeSort(arr, low, high):
    if low >= high:
        return
    
    mid = low + (high-low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)



"""
    Selection Sort
"""

def selectionSort(arr):
    n = len(arr)

    # iterate over all the elements except the last one
    for i in range(n-1):
        # set the ith index as the one containing the minimum element in the unsorted array
        min_index = i

        # iterate over all the elements after i till the last element
        for j in range(i+1, n):
            # check if jth element is smaller that min index element
            if arr[j] < arr[min_index]:
                # set the min index as j
                min_index = j

        # swap the min index with the ith index
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr 


"""
Insertion Sort
"""

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]           # shifting elements
            j-=1
        arr[j+1] = key
    
    return arr


def get_subsets(lst):
    """
        function for generate all the subsets of a list
        [1, 2, 3]
        output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    """

    subset = []
    n = len(lst)

    for i in range(2**n):
        subsets = [lst[j] for j in range(n) if (i & (1<<j))]
        subsets.append(subset)