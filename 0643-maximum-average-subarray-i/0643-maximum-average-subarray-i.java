class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int windowSum = 0;
        int n = nums.length;

        // first window sum
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maxSum = windowSum;

        // sliding window
        for (int i = k; i < n; i++) {
            windowSum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, windowSum);
        }

        return (double) maxSum / k;
    }
}