class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        string_f = {}
        left = 0
        max_frequency = 0
        longest_length = 0

        for right in range(n):
            value = s[right]
            string_f[value] = string_f.get(value, 0) + 1
            max_frequency = max(max_frequency, string_f[value])

            while right - left + 1 - max_frequency > k:
                string_f[s[left]] -= 1
                left += 1

            window_length = right - left + 1
            longest_length = max(longest_length, window_length)

        return longest_length



    


                




            


        
       



