class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_length = 0
        max_frequency = 0
        window_frequency = {}

        for right in range(n):
            value = s[right]
            window_frequency[value] = window_frequency.get(value, 0) + 1
            max_frequency = max(max_frequency, window_frequency[value])

            while (right - left + 1 - max_frequency) > k:
                window_frequency[s[left]] -= 1
                left += 1

            window_length = right - left + 1
            max_length = max(window_length, max_length)

        return max_length




    


                




            


        
       



