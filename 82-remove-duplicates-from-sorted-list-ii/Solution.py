# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        datas = {}
        while p:
            if p.val not in datas.keys():
                datas[p.val] = 1
            else:
                datas[p.val] = datas[p.val] + 1
            p = p.next
        distinct_datas = []
        for k, v in datas.items():
            if v == 1:
                distinct_datas.append(k)

        head = None
        pre = None
        flag = True
        for data in distinct_datas:
            if flag:
                head = ListNode(data)
                pre = head
                flag = False
            else:
                pre.next = ListNode(data)
                pre = pre.next

        return head