class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1: return len(nums)

        nums.sort()
        n = len(nums)

        consecutive_hash = {}

        max_count = 0;
        current_count = 1

        consecutive_hash[nums[0]] = True

        for i in range(1, n):
            currentValue = nums[i]
            previousValue = nums[i - 1];
            equal = currentValue == previousValue
            greater_equal_one = currentValue - previousValue == 1
            
            if equal or greater_equal_one:
                if consecutive_hash.get(currentValue) is None:
                    consecutive_hash[currentValue] = True
                    current_count += 1 
                    
            else:
                consecutive_hash[currentValue] = True
                max_count = current_count if current_count > max_count else max_count
                current_count = 1
        
        max_count = current_count if current_count > max_count else max_count
        return max_count


