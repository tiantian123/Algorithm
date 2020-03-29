#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/29 11:14
# @Author: Tian Chen
# @File: Day14_169_MajorityCount.py
"""
169. Majority Count
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""
from typing import List
import collections


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        """ approach1: Map """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums: List[int]) -> int:
        """ approach2: Sort """
        sorted(nums)
        return nums[len(nums) // 2]

    def majorityElement3(self, nums: List[int]) -> int:
        """ approach3: Divide & Conquer"""
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        left = self.majorityElement3(nums[:len(nums)//2])
        right = self.majorityElement3(nums[len(nums)//2:])
        if left == right:
            return left
        return [right, left][nums.count(left) > len(nums) // 2]