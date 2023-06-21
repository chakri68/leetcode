from DataStructures.LinkedList import makeLinkedList, printLinkedList, ListNode
from typing import Optional


def reverseSubList(l: ListNode, k: int):
    head: ListNode = l
    tail: ListNode = head
    """
    Reverses the first k elements of a linked list with head at l and returns the head and tail of the reversed part
    """
    currNode = head.next
    ind = 1
    while currNode is not None and ind < k:
        tail.next = currNode.next
        currNode.next = head
        head = currNode
        currNode = tail.next
        ind += 1
    return head, tail


def getLength(l: ListNode):
    currNode: Optional[ListNode] = l
    s = 0
    while currNode is not None:
        currNode = currNode.next
        s += 1
    return s


def solution(l: ListNode, k: int):
    s = getLength(l)
    currNode: ListNode = l
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for i in range(s // k):
        smolHead, smolTail = reverseSubList(currNode, k)
        if tail is not None:
            tail.next = smolHead
        tail = smolTail
        if head is None:
            head = smolHead
        if smolTail.next is None:
            continue
        currNode = smolTail.next
    return head


printLinkedList(solution(makeLinkedList(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 0))
