class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for right in range(len(temperatures)):
            value = temperatures[right]
            while stack and value > temperatures[stack[-1]]:
                index = stack[-1]
                result[index] = right - index
                stack.pop()

            stack.append(right)

        return result
                


        
       

        