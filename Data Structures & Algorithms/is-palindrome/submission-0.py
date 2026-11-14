class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for letter in s:
            if letter.isalnum() == True:
                word.append(letter.lower())
            else:
                continue

        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False
                break
        return True
            

        

        