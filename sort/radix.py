def radix_sort(nums: list[int], inplace=False):
    md = len(str(max(nums)))
    cnums = list(
        map(
            lambda x: ("+" if x >= 0 else "-")
            + "0" * (md - len(str(abs(x))))
            + str(abs(x)),
            nums,
        )
    )

    for d in range(md, 0, -1):
        buckets = [[] for _ in range(10)]
        for cnum in cnums:
            buckets[int(cnum[d])].append(cnum)

        cnums.clear()
        for bucket in buckets:
            cnums.extend(bucket)

    # handling negative numbers
    buckets = {"+": [], "-": []}
    for cnum in cnums:
        buckets[cnum[0]].append(cnum)

    cnums.clear()
    cnums.extend(buckets["-"][::-1])
    cnums.extend(buckets["+"])

    if not inplace:
        nums = [int(cnum) for cnum in cnums]
    else:
        nums[:] = [int(cnum) for cnum in cnums]
    return nums
