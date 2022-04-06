# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    def __init__(self, node=None):
        self._head = node

    def