# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p = head
        datas = []
        dict = {}
        while p:
            datas.append(p.val)
            p = p.next
        n = len(datas)
        for i in range(0, len(datas)):
            new_i = (i + k) % n
            dict[new_i] = datas[i]
        list = sorted(dict.items())
        j = 0
        for elem in list:
            datas[j] = elem[1]
            j += 1
        p = head = None
        for data in datas:
            if p:
                p.next = ListNode(data)
                p = p.next
            else:
                p = head = ListNode(data)

        return head