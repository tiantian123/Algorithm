#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/27 0:55
# @Author: Tian Chen
# @File: 33_Rotated_array_find.py
"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if target == nums[mid]: return mid
            if nums[low] <= nums[mid]: # 左边不包含旋转数组
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


