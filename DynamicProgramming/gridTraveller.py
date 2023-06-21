from typing import Any, Callable, Dict


class memoize(object):
    def __init__(self, func: Callable[[int, int], int]):
        self.func = func
        self.cache: Dict[int, Dict[int, int]] = dict()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        m: int = args[0]
        n: int = args[1]
        if m in self.cache:
            if n in self.cache[m]:
                return self.cache[m][n]
        else:
            self.cache[m] = dict()
        value = self.func(m, n)
        self.cache[m][n] = value
        return value


@memoize
def gridTraveller(m: int, n: int):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return (gridTraveller(m - 1, n) + gridTraveller(m, n - 1))


print(gridTraveller(18, 18))
