class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=0
        n=len(nums)
        for i in nums:
            total+=i
        left=0
        for i in range(n):
            right=total-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1
s=Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
