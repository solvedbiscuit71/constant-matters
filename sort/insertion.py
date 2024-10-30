def insertion_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                break

    return nums
