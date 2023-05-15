def fibonacci(n, cache):
    # defining base cases
    if n <= 2:
        return 1

    if n in cache.keys():
        return cache[n]
    fib_n_minus_1 = fibonacci(n-1, cache)
    if n-1 not in cache.keys():
        cache[n-1] = fib_n_minus_1

    fib_n_minus_2 = fibonacci(n-2, cache)
    if n-2 not in cache.keys():
        cache[n-2] = fib_n_minus_2

    return fib_n_minus_1 + fib_n_minus_2


n = 100
cache = {}
fib_n = fibonacci(n, cache)
print(f"The fbonacci number for value {n} is {fib_n}")