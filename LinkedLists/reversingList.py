from DataStructures.LinkedList import ListNode, makeLinkedList, printLinkedList, Optional


def reverseLinkedList(l: ListNode):
    prevNode = None
    currNode = l
    while currNode is not None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    if prevNode is None:
        raise ValueError
    return prevNode
