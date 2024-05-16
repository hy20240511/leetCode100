# 题目：合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 输入：lists = []
# 输出：[]
# 输入：lists = [[]]
# 输出：[]
#
def ListNode(param):
    pass


def mergeKLists(self,lists):
    import heapq
    dummy = ListNode(0)
    p = dummy
    head = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next
    while head:
        val, idx = heapq.heappop(head)
        p.next = ListNode(val)
        p = p.next
        if lists[idx]:
            heapq.heappush(head, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
    return dummy.next
