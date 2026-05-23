class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # bruth force
        if s == ' ': return 1

        n = len(s)
        left = 0
        exist_values = {}
        current_length = 0
        max_length = 0
        for right in range(n):
            value = s[right]

            if value not in exist_values:
                exist_values[value] = True
            else:
                while True:
                    if value in exist_values:
                        del exist_values[s[left]]
                    else:
                        break;

                    left += 1

                exist_values[value] = True
                
            max_length = max(max_length, len(exist_values.keys()))

        return max_length
            

        





        



