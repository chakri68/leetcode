# Super useful resources
#   https://en.wikipedia.org/wiki/Weighted_median
#   https://en.wikipedia.org/wiki/Percentile#Weighted_percentile

from typing import List


def weighedMedian(nums: List[int], cost: List[int]) -> int:
    # Get the middle index
    approxMiddleInd = sum(cost) // 2
    arr = sorted(zip(nums, cost))
    c = 0
    target = 0
    for i, num in arr:
        c += i
        # as the array is sorted its better to go up for the result
        if c > approxMiddleInd:
            target = num
            break
    return target
