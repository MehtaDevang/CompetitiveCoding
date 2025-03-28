class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in mapper:
                return [mapper[remainder], index]
            else:
                mapper[num] = index
        return []