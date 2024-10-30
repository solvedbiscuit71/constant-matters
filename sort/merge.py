def merge_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid], inplace=True)
    right = merge_sort(nums[mid:], inplace=True)

    def merge():
        i = 0
        l, r = 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[i] = left[l]
                l += 1
            else:
                nums[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            nums[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            nums[i] = right[r]
            r += 1
            i += 1

    merge()
    return nums
