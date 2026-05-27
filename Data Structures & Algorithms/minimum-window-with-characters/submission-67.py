class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f_values = {}
        for i in range(len(t)):
            f_values[t[i]] = f_values.get(t[i], 0) + 1

        current_count = {}
        target = len(f_values)
        current_target = 0
        target_string = ""
        left = 0

        for right in range(len(s)):
            value = s[right]
            current_count[value] = current_count.get(value, 0) + 1

            if current_count[value] == f_values.get(value, 0):
                current_target += 1

            while current_target == target:
                # shrink left
                current_string = ""
                k = left
                while k <= right:
                    current_string += s[k]
                    k += 1

                if len(target_string) == 0:
                    target_string = current_string
                else:
                    target_string = current_string if len(current_string) < len(target_string) else target_string
                    
                left_value = s[left]
                current_count[left_value] -= 1
                
                if left_value in f_values and current_count[left_value] <  f_values[left_value]:
                    current_target -= 1

                left += 1

        return target_string



    

                

        

        

        