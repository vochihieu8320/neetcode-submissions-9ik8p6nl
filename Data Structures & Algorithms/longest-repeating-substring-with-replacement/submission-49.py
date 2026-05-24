class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        frequency = {}
        max_f = 0
        left = 0
        max_length = 0;

        for right in range(n):
            value = s[right]
            frequency[value] = frequency.get(value, 0) + 1
            max_f = frequency[value] if frequency[value] > max_f else max_f
            
            window_valid = right - left + 1 - max_f <= k
            if window_valid:
                substring = right - left + 1;
                max_length = max(max_length, substring)
            else:
                while left < right and right - left + 1 - max_f > k:
                    frequency[s[left]] =  frequency[s[left]] - 1
                    updated_max_f = 0
                    for key in frequency.keys():
                        updated_max_f = frequency[key] if frequency[key] > updated_max_f else updated_max_f

                    left += 1
                    max_f = updated_max_f

        return max_length
                




            


        
       



