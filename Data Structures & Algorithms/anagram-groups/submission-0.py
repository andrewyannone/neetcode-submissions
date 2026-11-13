class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for words in strs:
            word = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for letters in words:
                word[ord(letters)-97] += 1
            word = tuple(word)
            if word in word_dict:
                word_dict[word].append(words) 
            else:
                word_dict[word] = [words]
        # print(word_dict)
        final_list = []
        for values in word_dict:
            final_list.append(word_dict[values])
        return final_list
    
            
        