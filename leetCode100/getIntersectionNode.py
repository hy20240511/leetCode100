# 题目：相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 图示两个链表在节点 c1 开始相交：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Intersected at '2'
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
from typing import List

def getIntersectionNode(headA,headB):
    PA = headA
    PB = headB
    if PA == None or PB == None:
        return None
    while PA != PB:
        PA = headB if PA == None else PA.next
        PB = headA if PB == None else PB.next
    return PB

