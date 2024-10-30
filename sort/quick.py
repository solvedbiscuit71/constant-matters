def quick_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    if len(nums) < 2:
        return nums

    def partition():
        key = nums[-1]
        i = 0
        for j in range(len(nums) - 1):
            if nums[j] < key:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[-1] = nums[-1], nums[i]
        return i

    p = partition()
    nums[:p] = quick_sort(nums[:p], inplace=True)
    nums[p + 1 :] = quick_sort(nums[p + 1 :], inplace=True)

    return nums
