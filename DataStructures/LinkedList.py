from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, x: T):
        self.value: T = x
        self.next: Optional[ListNode] = None

    def __str__(self) -> str:
        return str(self.value)


def makeLinkedList(l: List) -> ListNode:
    head = None
    tail = None
    for i in l:
        newNode = ListNode(i)
        if tail is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
    if head is None:
        raise ValueError
    return head


def printLinkedList(l: Optional[ListNode]):
    res = []
    currNode = l
    while currNode is not None:
        res.append(currNode.value)
        currNode = currNode.next
    print(res)


def getLength(l: Optional[ListNode]):
    length = 0
    currNode = l
    while currNode is not None:
        length += 1
    return length
