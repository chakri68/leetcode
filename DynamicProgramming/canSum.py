from typing import List,  Dict, Optional


def canSum(targetSum: int, numbers: List[int], cache: Optional[Dict[int, bool]] = None):
    if cache is None:
        cache = {}
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    res = False
    for i in numbers:
        if targetSum - i in cache:
            res = res or cache[targetSum - i]
        else:
            res = res or canSum(targetSum - i, numbers, cache)
        if res:
            break
    cache[targetSum] = res
    return res


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [2, 7]))
