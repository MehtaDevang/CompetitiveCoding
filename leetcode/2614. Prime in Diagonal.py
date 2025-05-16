"""
You are given a 0-indexed two-dimensional integer array nums.
Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:
    An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
    An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.

Example 1:
    Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
    Output: 11
    Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.

Example 2:
    Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
    Output: 17
    Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
 
Constraints:
    1 <= nums.length <= 300
    nums.length == numsi.length
    1 <= nums[i][j] <= 4*106
"""

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        max_prime_diagonal = 0

        def is_prime(num):
            if num == 1:
                return False
            if num == 2 or num == 3:
                return True
            
            for i in range(2, int(math.ceil(math.sqrt(num))) + 1):
                if num % i == 0:
                    return False
            return True
        
        def find_max_prime_diagonal(max_prime_diagonal):
            for i in range(n):
                n1 = nums[i][i]
                if is_prime(n1):
                    max_prime_diagonal = max(max_prime_diagonal, n1)
                
                n2 = nums[i][n-i-1]
                if is_prime(n2):
                    max_prime_diagonal = max(max_prime_diagonal, n2)
            return max_prime_diagonal
            
        return find_max_prime_diagonal(max_prime_diagonal)
