#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/23 20:32
# @Author: Tian Chen
# @File: Day10_Mid_Of_Linked_List.py
"""
876. Middle of Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Example:
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode1(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode2(self, head: ListNode) -> ListNode:
        # 遍历2遍
        cnt = 0
        pos = head
        while pos:
            pos = pos.next
            cnt += 1
        k, pos = 0, head
        while k < cnt // 2:
            k += 1
            pos = pos.next
        return pos