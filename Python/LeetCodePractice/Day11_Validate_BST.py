#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/26 23:43
# @Author: Tian Chen
# @File: Day11_Validate_BST.py
"""
98. Validate Binary Search Tree
"""


# Definition for binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        """ 中序遍历"""
        arr = self.inorders(root)
        return arr == list(sorted(set(arr)))

    def inorders(self, root):
        if root is None:
            return []
        return [self.inorders(root.left)] + [root.val] + [self.inorders(root.right)]

    def isValidBST2(self, root: TreeNode) -> bool:
        """中序遍历，仅记录父亲结点"""
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        """中序遍历"""
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.pre and self.pre.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

    def isValidBST3(self, root: TreeNode) -> bool:
        """Recursion """
        def comupute_BST(root, min_ = float('-inf'), max_ = float('inf')):
            if root is None:
                return True
            if root.val < min_ or root.val > max_:
                return False
            if not comupute_BST(root.left, min_, root.val):
                return False
            if not comupute_BST(root.right, root.val, max_):
                return False
            return True
        return comupute_BST(root)