class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let existValue = {};
        let results = [];
        for (let i = 0; i < nums.length; i++) {
            const value = nums[i];
            if (existValue[value] != null) {
                existValue[value] += 1;
            } else {
                existValue[value] = 1
            }
        }

        // sort number of exists in desc and take first k value

        const firstK = Object.values(existValue).sort((a, b) => b - a).slice(0, k);
        Object.keys(existValue).forEach(value => {
            const frequency = existValue[value];
            if (firstK.includes(frequency)) results.push(value)
        })

        return results
    }
}
