class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        t = n * (n + 1) // 2
        sum = 0

        for i in nums:
            sum += i

        return t - sum

s = Solution()
print(s.missingNumber([3, 0, 1]))
