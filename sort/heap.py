def heap_sort(nums: list[int], inplace=False):
    if not inplace:
        nums = nums.copy()

    n = len(nums)

    def MCI(i: int) -> int:
        """
        MCI stands for (M)ax (C)hild (I)ndex
        returns the index of the max child for a given node
        """
        l, r = 2 * i + 1, 2 * i + 2
        return r if r < n and nums[r] > nums[l] else l

    def sink(i: int):
        c = MCI(i)
        while c < n and nums[c] > nums[i]:
            nums[i], nums[c] = nums[c], nums[i]
            i = c
            c = MCI(i)

    # heapify
    from math import floor, log2

    for i in range(pow(2, floor(log2(len(nums)))) - 2, -1, -1):
        sink(i)

    for _ in range(len(nums) - 1):
        nums[0], nums[n - 1] = nums[n - 1], nums[0]
        n -= 1
        sink(0)

    return nums
