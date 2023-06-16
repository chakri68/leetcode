from typing import List


def checkIncreasing(sequence: List[int]):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True


def solution(sequence: List[int]) -> bool:
    for i in (range(len(sequence) - 1)):
        if sequence[i] >= sequence[i + 1]:
            return (checkIncreasing(sequence[i + 1:]) if i - 1 < 0 or sequence[i + 1] > sequence[i - 1] else False) or checkIncreasing([sequence[i], *sequence[i + 2:]])
    return True


print(solution([3, 1, 2]))
