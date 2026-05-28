class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_f = {}
        for i in range(len(s1)):
            target_f[s1[i]] = target_f.get(s1[i], 0) + 1

        window_f = {}
        window_count = 0
        left = 0

        target_count = len(target_f)

        for right in range(len(s2)):
            value = s2[right]
            window_f[value] = window_f.get(value, 0) + 1
            if value in target_f and window_f[value] == target_f[value]:
                window_count += 1

            while right - left + 1 > len(s1):  
                value_left = s2[left]
              
                if value_left in target_f and window_f[value_left] == target_f[value_left]:
                    window_count -= 1   # about to drop below target

                window_f[value_left] -= 1

                left += 1

            if window_count == target_count:
                return True
 
        return False

        