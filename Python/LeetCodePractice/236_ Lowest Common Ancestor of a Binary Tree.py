#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/5/10 10:57
# @Author: Tian Chen
# @File: 236_ Lowest Common Ancestor of a Binary Tree.py
"""
236.  Lowest Common Ancestor of a Binary Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(self.left, p, q)
        right = self.lowestCommonAncestor(self.right, p, q)
        if left and right:
            return root
        return left if right is None else right
