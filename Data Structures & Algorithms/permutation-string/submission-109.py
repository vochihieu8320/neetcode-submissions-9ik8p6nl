class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        left = 0
        window_f = {}
        window_count = 0

        target_f = {}
        for i in range(len(s1)):
            target_f[s1[i]] = target_f.get(s1[i], 0) + 1

        target_count = len(target_f)

        for right in range(n):
            value = s2[right]
            window_f[value] = window_f.get(value, 0) + 1

            if window_f[value] == target_f.get(value):
                window_count += 1

            while right - left + 1 > len(s1):
                # shrink left
                left_value = s2[left]

                if left_value in target_f and window_f[left_value] == target_f[left_value]:
                    window_count -= 1

                window_f[left_value] -= 1
                left += 1

            if window_count == target_count:
                return True


        return False

        