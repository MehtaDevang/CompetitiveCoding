"""
write a function that takes in a target sum and a list of numbers as arguments
the function should return a list of any combination of elements that add upto the target sum.
If there is no combination that adds up to the target sum then return None
If there are multiple matches, you may return any single one
"""

def get_combinations(target_sum, numbers, cache={}):

    if target_sum < 0:
        return None
    if target_sum == 0:
        return []
    if target_sum in cache.keys():
        return cache[target_sum]

    for _number in numbers:
        updated_sum = target_sum - _number
        is_possible = get_combinations(updated_sum, numbers, cache)
        if is_possible is not None:
            is_possible.append(_number)
            cache[target_sum] = is_possible
            return is_possible

    cache[target_sum] = None
    return None

print(get_combinations(7, [2, 3], {}))
print(get_combinations(7, [5, 3, 4, 7], {}))
print(get_combinations(9, [2], {}))
print(get_combinations(8, [2, 3, 5], {}))
print(get_combinations(7, [2, 4], {}))
print(get_combinations(300, [7, 14], {}))

