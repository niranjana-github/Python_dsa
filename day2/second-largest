def second_largest(nums):
    largest = nums[0]
    second = None
    for i in nums:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if second is None or i > second:
                second = i
    return second
