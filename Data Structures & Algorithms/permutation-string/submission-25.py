class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        exist_values = {}
        for k in range(n1):
            exist_values[s1[k]] = exist_values.get(s1[k], 0) + 1

        for i in range(n2):
            j = i;
            max_loop = j + n1

            dup_exist_values = exist_values.copy()

            while j < max_loop and j < n2:
                value = s2[j]

                if value in dup_exist_values and dup_exist_values[value] > 0:
                    dup_exist_values[value] = dup_exist_values[value] - 1

                j += 1

            sum = 0
            for key in dup_exist_values.keys():
               sum += dup_exist_values[key]

            if sum == 0: return True

        return False



            



                
        