from typing import List, Dict, Union, Optional


def bestSum(targetSum: int, numbers: List[int], cache: Optional[Dict[int, Union[List[int], bool]]] = None) -> Union[List[int], bool]:
    if targetSum == 0:
        return []
    if targetSum < 0:
        return False
    if cache is None:
        cache = {}
    res = False
    for i in numbers:
        if targetSum - i in cache:
            toCheck = cache[targetSum - i]
        else:
            toCheck = bestSum(targetSum - i, numbers, cache)
        if isinstance(toCheck, list):
            if isinstance(res, list):
                if len(toCheck) + 1 < len(res):
                    res = [i, *toCheck]
            else:
                res = [i, *toCheck]
    cache[targetSum] = res
    return res


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))
