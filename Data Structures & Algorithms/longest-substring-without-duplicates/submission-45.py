class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        left = 0
        exist_values = {}
        for right in range(n):
            value = s[right]
            if value not in exist_values:
                exist_values[value] = True
            else:
                # shrink left
                while value in exist_values:
                    exist_values.pop(s[left], None)
                    left += 1

                exist_values[value] = True

            max_length = max(max_length, right - left + 1)

        return max_length

                


            

        





        



