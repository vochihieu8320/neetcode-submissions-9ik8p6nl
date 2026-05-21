import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_splited = s.split(" ")
        downcase_s = "";

        for i in range(len(string_splited)):
            cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', string_splited[i].lower())
            downcase_s +=  cleaned

        for i in range(len(downcase_s)):
            if downcase_s[i] != downcase_s[len(downcase_s) - 1 - i]: return False

        return True
        
        