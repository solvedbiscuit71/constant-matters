def bubble_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    for n in range(len(nums), -1, -1):
        swapped = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                swapped = True
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        if not swapped:
            break

    return nums
