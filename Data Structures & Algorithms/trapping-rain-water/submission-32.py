class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0;

        # precompute left max arrays

        left_max_arrays = [0] * n
        right_max_arrays = [0] * n

        left_max_arrays[0] = height[0]
        for i in range(1, n):
            left_max_arrays[i] = max(left_max_arrays[i - 1], height[i])

        right_max_arrays[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max_arrays[i] = max(right_max_arrays[i + 1], height[i])

        for i in range(0, n):
            max_left = left_max_arrays[i]
            max_right = right_max_arrays[i]
            water = min([max_left, max_right]) - height[i]
            if water > 0: max_water += water

        return max_water

