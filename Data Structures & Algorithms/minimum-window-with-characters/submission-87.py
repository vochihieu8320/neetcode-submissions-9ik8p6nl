class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_f = {}

        for i in range(len(t)):
            target_f[t[i]] = target_f.get(t[i], 0) + 1

        target_count = len(target_f)

        window_f = {}
        window_count = 0

        min_left = None
        min_right = None
        left = 0

        for right in range(len(s)):
            value = s[right]
            window_f[value] = window_f.get(value, 0) + 1

            if value in target_f and window_f[value] == target_f[value]:
                window_count += 1

            while window_count == target_count:
                if min_left is None and min_right is None:
                    min_left = left
                    min_right = right
                else:
                    window_distance = right - left + 1
                    target_distance = min_right - min_left + 1
                    if window_distance < target_distance:
                        min_left = left
                        min_right = right

                # shrink left
                left_value = s[left]
        
                if left_value in target_f and window_f[left_value] == target_f[left_value]:
                    window_count -= 1

                window_f[left_value] -= 1
                left += 1       

        target_string = ""
        if min_left is not None and min_right is not None:
            for i in range(min_left, min_right):
                target_string += s[i]

            target_string += s[min_right]

        return target_string

 
        




    

                

        

        

        