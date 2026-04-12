class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let existNumber = {};
        for (let i = 0; i < nums.length; i++) {
            const value = nums[i];
            if (existNumber[value] != null) return true;

            existNumber[value] = 1
        }

        return false
    }
}
