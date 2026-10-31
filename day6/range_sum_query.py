class NumArray:
    def __init__(self, nums: list[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        total=0
        for i in range(left,right+1):
            total+=self.nums[i]
        return total
obj=NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
