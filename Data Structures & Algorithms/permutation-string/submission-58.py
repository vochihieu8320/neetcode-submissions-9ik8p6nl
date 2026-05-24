class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        exist_values = {}
        for i in range(n1):
            exist_values[s1[i]] = exist_values.get(s1[i], 0) + 1

        right = 0
        while right <= n2 - n1:
            j = 0
            frequency = exist_values.copy()
            length = 0
            while j < n1:
                value = s2[right + j]
                if value in frequency and frequency[value] > 0:
                    frequency[value] = frequency[value] - 1
                    length += 1

                j += 1

            if length == n1:
                return True

            right += 1
            
        return False;

        