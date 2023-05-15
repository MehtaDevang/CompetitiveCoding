# we can only traverse one step to the right or down
def traverse(i, j, m, n, result, cache):
    # defining base cases
    if i >= m:
        return 0
    if j >= n:
        return 0
    if (i, j) in cache.keys():
        return cache[(i,j)]
    if i == m-1 and j == n-1:
        return 1

    # second operand is for moving down one step
    # third operand is for moving right one step
    # result = traverse(i+1, j, m, n, result) + traverse(i, j+1, m, n, result)
    down_traversal = traverse(i+1, j, m, n, result, cache)
    if (i+1, j) not in cache.keys():
        cache[(i+1, j)] = down_traversal
    right_traversal = traverse(i, j+1, m, n, result, cache)
    if (i, j+1) not in cache.keys():
        cache[(i, j+1)] = right_traversal

    return result + down_traversal + right_traversal

def start_traversal(m, n):
    # we will be starting at the top left corner of the grid
    # initially we have 0 ways of traversing
    result = 0
    i = 0
    j = 0
    cache = {}
    return traverse(i, j, m, n, result, cache)

m = 20
n = 20
print(m, n, start_traversal(m, n))