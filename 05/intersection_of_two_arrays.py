
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in result:
                        result += [i]
                    break

        return result

s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))

