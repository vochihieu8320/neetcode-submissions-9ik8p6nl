class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures);
        result = [0] * n

        for i in range(n):
            current_temp = temperatures[i]
            for j in range(i, n):
                if temperatures[j] > current_temp:
                    result[i] = j - i
                    break;

        
        return result

        