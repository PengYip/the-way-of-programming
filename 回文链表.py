# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def lenth(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next  # 游标往后移
        return count

    def travel(self):
        """遍历元素"""
        cur = self._head
        while cur != None:
            print(cur.val)
            cur = cur.next

    def add(self, item):
        pass

    def append(self, item):
        """尾部添加元素"""
        node = ListNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


if __name__ == "__main__":
    ll = LinkList()
    print(ll.is_empty())
    print(ll.lenth())
    ll.append(100)
    print(ll.is_empty())
    print(ll.lenth())
    ll.append(99)
    ll.append(98)
    ll.append(97)
    ll.travel()

    def __del__(self):

    def __index__(self):
