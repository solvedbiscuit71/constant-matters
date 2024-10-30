def selection_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    for i in range(len(nums) - 1):
        min_i = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]

    return nums
