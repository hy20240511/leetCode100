# 题目：两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 输入：head = []
# 输出：[]
# 输入：head = [1]
# 输出：[1]

def swapPairs(self,head):
    if not head or not head.next:
        return head
    newHead = head.next
    head.next = self.swapPairs(newHead.next)
    newHead.next = head
    return newHead

