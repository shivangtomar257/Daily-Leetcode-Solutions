class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        totalSum = prefix[n - 1]

        for i in range(n):
            left = prefix[i-1] if i>0 else 0
            right = totalSum - prefix[i]
            if left == right:
                return i
        return -1