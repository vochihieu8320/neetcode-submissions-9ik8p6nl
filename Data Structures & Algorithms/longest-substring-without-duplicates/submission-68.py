class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        window_f = {}
        max_length = 0

        for right in range(n):
            value = s[right]
            while value in window_f:
                window_f.pop(s[left], None)
                left += 1

            window_f[value] = True
            window_length = right - left + 1
            max_length = max(max_length, window_length)

        return max_length

        


        

            

                


            

        





        



