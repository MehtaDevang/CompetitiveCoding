"""
write a function that takes in a target sum and a list of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to generate the target sum
using numbers from the list
"""


def is_possible(target_sum, numbers, cache = {}):
    # defining the base cases

    if target_sum in cache.keys():
        return cache[target_sum]
    if target_sum == 0:
        return True
    if len(numbers) == 0:
        return False
    if target_sum < 0:
        return False

    for _number in numbers:
        updated_sum = target_sum - _number
        # possible = is_possible(updated_sum, numbers, cache)
        if is_possible(updated_sum, numbers, cache):
            cache[target_sum] = True
            return True

    cache[target_sum] = False
    return False


print(is_possible(7, [2, 3], {}))
print(is_possible(7, [5, 3, 4, 7], {}))
print(is_possible(7, [2, 4], {}))
print(is_possible(8, [2, 3, 5], {}))
print(is_possible(300, [7, 14], {}))