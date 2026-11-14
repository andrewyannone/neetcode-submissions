class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        sum_full = sum(range(0, n+1))
        return sum_full - sum_nums