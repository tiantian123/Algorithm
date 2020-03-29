#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/29 18:08
# @Author: Tian Chen
# @File: Day16_102_BTLevelOrder.py
"""
102. Binary Tree level order
"""
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)

        visited = set(root)
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level)
        return result
