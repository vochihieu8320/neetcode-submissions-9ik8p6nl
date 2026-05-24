class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        frequency_values = {}
        count_values = {}
        for i in range(n1):
            frequency_values[s1[i]] = frequency_values.get(s1[i], 0) + 1
            count_values[s1[i]] = 0

        matches = 0
        left = 0
        total = len(frequency_values)

        for right in range(n2):
            value = s2[right]

            if value in count_values:
                count_values[value] += 1

                if count_values[value] == frequency_values[value]:
                    matches += 1
        
            if matches == total:
                return True

            # shrink left
            if right - left + 1 == n1:
                old = s2[left]
                if old in count_values:
                    if count_values[old] == frequency_values[old]:
                        matches -= 1
                    count_values[old] -= 1
                left += 1
        
            
        return False;

        