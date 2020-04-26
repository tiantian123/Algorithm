#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/27 0:12
# @Author: Tian Chen
# @File: 23_Merged_sorted_list.py
"""
23. Merge K sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
 """
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return -1
        n = len(lists)
        return self.merge(lists, 0 , n-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + ((right - left) >> 1)
        list1 = self.merge(lists, left, mid)
        list2 = self.merge(lists, mid + 1, right)
        return self.merge2lists(list1, list2)

    def merge2lists(self, lists1, lists2):
        if not lists1: return lists2
        if not lists2: return lists1
        if lists1.val < lists2.val:
            lists1.next = self.merge2lists(lists1.next, lists2)
            return lists1
        else:
            lists2.next = self.merge2lists(lists2.next, lists1)
            return lists2
