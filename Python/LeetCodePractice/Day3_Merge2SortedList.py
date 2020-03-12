#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/12 21:04
# @Author: tiantian
# @File: Day3_Merge2SortedList.py
"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two list.
example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Recursively
        :param l1: list1
        :param l2: list2
        :return: MergedList
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeTwoLists2(self, l1:ListNode, l2: ListNode) -> ListNode:
        """
        iteratively
        """
        prehead = ListNode(-1)

        pre = prehead
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        pre.next = l1 if l1 is not None else l2
        return prehead.next

    def mergeTwoList3(self, l1: ListNode, l2: ListNode) -> ListNode:
        # in-place, iteratively
        if None in (l1, l2):
            return l1, l2
        dummy = cur = ListNode(0)
        while l1 and l2:
            cur.next = l1
            if l1.val < l2.val:
                l1 = l1.next
            else:
                tmp = l2.next
                cur.next = l2
                l2.next = l1
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
