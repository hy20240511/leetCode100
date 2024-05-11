# 题目：删除链表的倒数第N个节点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 输入：head = [1], n = 1
# 输出：[]
# 输入：head = [1,2], n = 1
# 输出：[1]

def ListNode(param, head):
    pass


def removeNthFromEnd(head,n):
    def getlength(head):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length

    length = getlength(head)
    dummy = ListNode(0,head)
    cur = dummy
    for i in range(1,length-n+1):
        cur = cur.next
    cur.next = cur.next.next
    return dummy.next
