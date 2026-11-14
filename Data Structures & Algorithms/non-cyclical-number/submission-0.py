class Solution:
    def isHappy(self, n: int) -> bool:
        sum_n= n
        tracker_set=set()
        while sum_n != 1:
            new_n = str(sum_n)
            sum_n = 0
            for i in new_n:
                sum_n += int(i)**2
            if sum_n in tracker_set:
                return False
                break

            else:
                tracker_set.add(sum_n)
        return True

        