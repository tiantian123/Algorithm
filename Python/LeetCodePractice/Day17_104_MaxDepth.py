#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/29 18:24
# @Author: Tian Chen
# @File: Day17_104_MaxDepth.py
"""
104. Max depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
"""
import collections

# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaxDepth:
    def maxDepth1(self, root: TreeNode) ->int:
        # Recursion
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(selfs, root: TreeNode) -> int:
        # BFS
        if not root:
            return 0
        queue = [(1,root)]
        while queue:
            depth, node = queue.pop(0) # 这个地方需要先遍历根节点
            if node.left: queue.append((depth+1, node.left))
            if node.right: queue.append((depth+1, node.right))
        return depth

    def maxDepth3(self, root: TreeNode) -> int:
        # DFS: 需要用max判断，DFS（先序遍历）节点右孩子先入栈，左孩子再入栈（先进后出）
        if not root:
            return 0
        queue = [(1, root)]
        max_depth = 0
        while queue:
            cur_depth, node = queue.pop()
            max_depth = max(max_depth, cur_depth)
            if node.right:
                queue.append((cur_depth + 1, node.right))
            if node.left:
                queue.append((cur_depth + 1, node.left))
        return max_depth


class MinDepth:
    def minDepth(self, root: TreeNode) -> int:
        # Recursion
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right + 1 if not left or not right else min(left, right) + 1

