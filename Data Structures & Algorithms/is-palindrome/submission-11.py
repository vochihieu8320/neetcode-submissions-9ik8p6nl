import re
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_splited = s.split(" ")
        normalize_string = ""
        for i in range(len(string_splited)):
            normalize_string += re.sub(r'[^a-zA-z0-9]', '', string_splited[i].lower())

        mid = math.ceil( len(normalize_string) / 2 )
     
        for i in range(0, mid):
            if normalize_string[i] != normalize_string[len(normalize_string) - 1 - i]:
                return False
        
        return True
      
        
        