from typing import Tuple


def helper(inputString: str) -> Tuple[str, int]:
    res = ""
    i = 0
    while i < len(inputString):
        c = inputString[i]
        if c == "(":
            s, ii = helper(inputString[i + 1:])
            res = s[::-1] + res
            i += ii + 1
        elif c == ")":
            return res, i + 1
        else:
            res = c + res
            i += 1
    return res, i + 1


def solution(inputString: str):
    res = ""
    ind = 0
    while ind < len(inputString):
        c = inputString[ind]
        if c == "(":
            s, ii = helper(inputString[ind + 1:])
            res = res + s
            ind += ii + 1
        else:
            ind += 1
            res = res + c
    return res


print(solution("foo(bar(baz))blim"))
