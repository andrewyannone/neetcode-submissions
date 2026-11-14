class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:       
        final_tally = 0
        set_nums = set(nums)
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            else:
                start = 1
                current_num = num
                while current_num + 1 in set_nums:
                    start += 1
                    current_num += 1
            if final_tally < start:
                final_tally = start
        
        return final_tally
            

