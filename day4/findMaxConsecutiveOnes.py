class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max=0
        c=0
        for i in nums:
            if i==1:
                c+=1
            if c>max:
                max=c
            if i==0:
                c=0
                
        return max
s=Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))
