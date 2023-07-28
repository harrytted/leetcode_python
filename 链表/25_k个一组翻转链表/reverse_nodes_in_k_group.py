# coding: utf-8

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 给定这个链表：1->2->3->4->5
# 输出
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 当 k = 3 时，应当返回: 3->2->1->4->5

# 解题思路
# 每次翻转前，确定翻转链表的范围，通过k循环来确定
# 记录翻转链表前驱和后继，方便翻转完成后把已翻转部分和未翻转部分连接起来
# 初始需要两个变量 pre 和 end，pre 代表待翻转链表的前驱，end 代表待翻转链表的末尾
# 经过k循环，end 到达末尾，记录待翻转链表的后继 next = end.next
# 翻转链表，然后将三部分链表连接起来，然后重置 pre 和 end 指针，然后进入下一次循环
# 特殊情况，当翻转部分长度不足 k 时，在定位 end 完成后，end==null，已经到达末尾，说明题目已完成，直接返回即可


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, tail = dummy, dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail: break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                # pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head
            tail = head
        return dummy.next
