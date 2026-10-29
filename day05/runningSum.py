class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l=[0]*n
        current_no=0
        for i in range(n):
            current_no+=nums[i]
            l[i]=current_no
        return l

s = Solution()
print(s.runningSum([1, 2, 3, 4]))
