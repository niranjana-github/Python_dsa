
class Solution:
    def frequencyCount(self, nums: list[int]) -> list[int]:
      n=len(nums)
      l=[]
      for i in range(1,n+1):
        c=0
        if i in nums:
          c+=1
        else:
          return 0 



soln = Solution()
print(soln.frequencyCount([2, 3, 3, 2, 5]))
