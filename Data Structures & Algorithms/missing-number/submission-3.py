class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for target in range(0,max(nums_set)):
            if target in nums:
                continue
            else:
                return target
                break
        return max(nums_set)+1
