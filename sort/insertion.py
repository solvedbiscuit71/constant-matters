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


def upper_bound(nums: list[int], key: int, n: int | None = None):
    if n is None:
        n = len(nums)

    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > key:
            r = mid
        else:
            l = mid + 1
    return r


def binary_insertion_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    for i in range(1, len(nums)):
        key = nums[i]
        k = upper_bound(nums, key, i)
        for j in range(i, k, -1):
            nums[j] = nums[j - 1]
        nums[k] = key
    return nums
