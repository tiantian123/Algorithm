#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/5/11 7:40
# @Author: Tian Chen
# @File: 25_Reverse Nodes in k-Group.py
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = self
        dummy.next = l = r = head
        while True:
            cnt = 0
            while r and cnt < k:
                # 移动 k 个步长，截取k个长度的子链表
                r = r.next
                cnt += 1
            if cnt == k:
                prev, cur = r, l
                for _ in range(k):
                    # 常规翻转链表
                    cur.next, prev, cur = prev, cur, cur.next
                # 将翻转的子链表与下一个链表进行链接
                jump.next, jump, l = prev, l, r
            else:
                return dummy.next
