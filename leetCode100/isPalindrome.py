# 题目：回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为
# 回文链表。如果是，返回 true ；否则，返回 false 。
# 输入：head = [1,2,2,1]
# 输出：true
# 输入：head = [1,2]
# 输出：false

def isPalindrome(head):
    if not head:
        return None
    vals = []
    current_node = head
    while current_node != None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]