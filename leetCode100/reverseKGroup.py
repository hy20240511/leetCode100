# 题目：K 个一组翻转链表
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]

def reverse(self, head, tail):
    prev = tail.next
    p = head
    while prev != tail:
        nex = p.next
        p.next = prev
        prev = p
        p = nex
    return tail, head

def reverseKGroup(self,head,k):
    hair = (0)
    hair.next = head
    pre = hair

    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next
        nex = tail.next
        head, tail = self.reverse(head, tail)
        pre.next = head
        tail.next = nex
        pre = tail
        head = tail.next

    return hair.next
