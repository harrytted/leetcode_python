"""
2、两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""

# 迭代
# 迭代的思路是，初始化答案为一个「空链表」，每次循环，向该链表末尾添加一个节点（保存一个数位）
# 循环遍历l1, l2, 每次把两个节点值l1.val,l2.val与进位值carry相加，除以 10 的余数即为当前节点需要保存的数位，除以10的商即为新的进位值。
# 需要注意的是，在第一次循环时，我们无法往一个空节点的末尾添加节点。这里的技巧是，创建一个哨兵节点（dummy node），
# 当成初始的「空链表」。循环结束后，哨兵节点的下一个节点就是最终要返回的链表头节点。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            add = l1_val + l2_val + carry
            carry = 1 if add >= 10 else 0
            add = add - 10 if add >= 10 else add
            cur.next = ListNode(add)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode()
    node1 = ListNode(2)
    l1.next = node1
    prev_node = node1
    node2 = ListNode(4)
    prev_node.next =node2
    prev_node = node2
    node2.next = ListNode(3)

    l2 = ListNode()
    node1 = ListNode(5)
    l2.next = node1
    prev_node = node1
    node2 = ListNode(6)
    prev_node.next = node2
    prev_node = node2
    node2.next = ListNode(4)

    pp = Solution().addTwoNumbers(l1, l2)
    while pp:
        print(pp.val)
        pp = pp.next


