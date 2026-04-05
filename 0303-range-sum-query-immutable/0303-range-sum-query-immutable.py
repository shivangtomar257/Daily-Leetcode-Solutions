class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]
        for i in range(1,n):
            self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left - 1] if left>0 else self.prefix[right]
