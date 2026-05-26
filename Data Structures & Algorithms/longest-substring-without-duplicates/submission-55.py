class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        left = 0
        charSet = set()

        for right in range(n):
            value = s[right]
            while value in charSet:
                charSet.remove(s[left])
                left += 1
    
            charSet.add(value)
            max_length = max(max_length, right - left + 1)

        return max_length 


            

                


            

        





        



