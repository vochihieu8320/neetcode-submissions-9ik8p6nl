class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f_values = {}
        min_string = ""

        for i in range(len(t)):
            f_values[t[i]] = f_values.get(t[i], 0) + 1

        t_length = len(f_values)
        print("f_values", f_values)

        for i in range(len(s)):
            current_count = 0
            current_f = {}
            current_string = ""

            j = i
            while j >= 0:
                value = s[j]
                current_f[value] = current_f.get(value, 0) + 1
                if value in f_values and current_f[value] == f_values[value]:
                    current_count += 1

                current_string = value + current_string
                if current_count == t_length:
                    if len(min_string) == 0:
                        min_string = current_string
                    else:
                        min_string = current_string if len(current_string) < len(min_string) else min_string
                        break

                j -= 1


        return min_string


                

        

        

        