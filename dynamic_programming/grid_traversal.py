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

    # first operand is for moving down one step
    # second operand is for moving right one step
    cache[(i, j)] = traverse(i+1, j, m, n, result, cache) + traverse(i, j+1, m, n, result, cache)
    return cache[(i, j)]

def start_traversal(m, n):
    # we will be starting at the top left corner of the grid
    # initially we have 0 ways of traversing
    result = 0
    i = 0
    j = 0
    cache = {}
    return traverse(i, j, m, n, result, cache)

m = 18
n = 18
print(m, n, start_traversal(m, n))