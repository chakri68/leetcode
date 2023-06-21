# from __future__ import annotations
from typing import Optional


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left: Optional[Tree] = None
        self.right: Optional[Tree] = None


def solution(t: Tree, s: int) -> bool:
    if t.left is None and t.right is None:
        if s == t.value:
            return True
        else:
            return False
    res = False
    if not res and t.left is not None and solution(t.left, s - t.value):
        res = True
    if not res and t.right is not None and solution(t.right, s - t.value):
        res = True
    return res


def makeTree(t):
    currNode = Tree(t["value"])


print()
