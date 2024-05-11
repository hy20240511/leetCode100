# 题目：反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 输入：head = [1,2]
# 输出：[2,1]
# 输入：head = []
# 输出：[]

def reverseList(head):
    if head == None:
        return None
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

