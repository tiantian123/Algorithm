#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/13 22:39
# @Author: Tian Chen
# @File: Day4_Merged2SortedArr.py
"""
88. Merge sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        1) Traverse 2 nums, Time: O((m+n)*log(m+n), space:O(1)
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        2) 2 pointer, from forward to back. Time: O(m+n), space:O(m)
        """
        temp = nums1[:m]
        nums1[:] = []
        p = 0
        q = 0
        while p < m and q < n:
            if temp[p] < nums2[q]:
                nums1.append(temp[p])
                p += 1
            else:
                nums1.append(nums2[q])
                q += 1
        if p < m:
            nums1[p+q:] = temp[p:]
        if q < n:
            nums1[p+q:] = nums2[q:]

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        3) 2 pointer, from back to forward. Time: O(m+n), space:O(m)
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]