class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_pairs = {}
        value_pair_list = []
        for position, number in enumerate(nums):
            difference = target - number
            if difference not in value_pairs:
                value_pairs[number] = position
            else:
                value_pair_list.append((value_pairs[difference]))
                value_pair_list.append(position)
                break
        
        return value_pair_list
                


        
        # for i in value_pairs:
            
           
        #     elif difference in value_pairs:
        #         value_pair_list.append(value_pairs[i])
        #         value_pair_list.append(value_pairs[difference])
        #         return value_pair_list
        #         break
     
            

 

        
        