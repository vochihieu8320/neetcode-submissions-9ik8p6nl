class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # bruth force
        if s == ' ': return 1

        exist_values = {}
        max_length = 0
        n = len(s)
        for i in range(n):
            current_length = 0
            for j in range(i, n):
                value = s[j]
                if value not in exist_values:
                    exist_values[value] = True
                    current_length += 1
                else:
                    exist_values = {}
                    break;

            max_length = max(max_length, current_length)

        return max_length




        



