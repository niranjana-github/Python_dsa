class Solution:
    def nonrepeatingElement(self, nums: list[int]) -> int:
      for i in nums:
        c=0
        for j in nums:
          if i==j:
            c+=1
        if c==1:
          return i
      return -1
      
soln=Solution()
print(soln.nonrepeatingElement([4, 5, 1, 2, 1, 4]))
