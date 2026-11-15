class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            answer = []
            left = 0
            right = len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] > target:
                    right -= 1
                elif numbers[left] + numbers[right] < target:
                    left +=1
                else:
                    answer.append(left+1)
                    answer.append(right+1)
                    return answer
                    break


        