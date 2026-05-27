class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f_values = {}
        for i in range(len(t)):
            f_values[t[i]] = f_values.get(t[i], 0) + 1

        min_left = None
        min_right = None
        min_distance = 0

        window_f = {}
        window_count = 0
        target_count = len(f_values)

        left = 0

        for right in range(len(s)):
            value = s[right]
            window_f[value] = window_f.get(value, 0) + 1
            if window_f[value] == f_values.get(value, 0):
                window_count += 1

            while window_count == target_count:
                distance = right - left + 1
                if min_distance == 0 or distance < min_distance:
                    min_distance = distance
                    min_left = left
                    min_right = right

                left_value = s[left]
                window_f[left_value] -= 1

                if left_value in f_values and window_f[left_value] < f_values[left_value]:
                    window_count -= 1

                left += 1


        target_string = ""

        if min_right is not None and min_left is not None:
            for i in range(min_left, min_right):
                target_string += s[i]

            target_string += s[min_right]

        return target_string
        




    

                

        

        

        