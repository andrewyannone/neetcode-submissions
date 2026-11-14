class Solution:
    def isValid(self, s: str) -> bool:
        stack_checker = []
        symbol_dict = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        for i in s:
            if i not in symbol_dict:
                stack_checker.append(i)
            else:
                if not stack_checker:
                    return False
                else:
                    symbol_check = stack_checker.pop()
                    if symbol_check != symbol_dict[i]:
                        return False
        if not stack_checker:
            return True
        else:
            return False
        
       
         

        



        