class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0
        
        for i in range(n):
            current_length = 0
            current_replace = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    current_length += 1
                elif s[j] != s[i] and current_replace < k:
                    current_length += 1
                    current_replace += 1
                else:
                    break

            if current_replace < k and i >= 1:
                right = i
                print("right", right)
                print("current_replace", current_replace)
                print("current_length", current_length)
                while right > 0 and current_replace < k:
                    current_length += 1
                    current_replace += 1
                    right -= 1

                print("after length", current_length)
                print("=====")

            max_length = max(current_length, max_length)

        return max_length



