# 题目：合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：输入：l1 = [], l2 = [0]
# 输出：[0]

def mergeTwoLists(list1,list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next,list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1,list2.next)
        return list2
