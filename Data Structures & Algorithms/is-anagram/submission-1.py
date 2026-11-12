class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict_s = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in count_dict_s:
                count_dict_s[i] += 1
            else:
                count_dict_s[i] = 1
        
        count_dict_t = {}
        for k in t:
            if k in count_dict_t:
                count_dict_t[k] += 1
            else:
                count_dict_t[k] = 1
        
        if count_dict_t == count_dict_s:
            return True
        else:
            return False

