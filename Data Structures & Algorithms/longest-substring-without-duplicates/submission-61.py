class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        max_length = 0
        string_f = {}

        for right in range(n):
            value = s[right]

            while value in string_f:
                string_f.pop(s[left], None)
                left += 1

            string_f[value] = True
            window_length = (right - left) + 1
            max_length = max(window_length, max_length)

        return max_length


            

                


            

        





        



