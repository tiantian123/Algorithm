#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/20 6:36
# @Author: Tian Chen
# @File: 42_Trapping_Rain_Water.py
"""
42. Trapping rain water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
 it is able to trap after raining
 Example:
     Input: [0,1,0,2,1,0,1,3,2,1,2,1]
     Output: 6
"""
from typing import List


class Solution1:
    """双指针法
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n =len(height)
        left, right = 0, n-1
        max_left, max_right = 0, 0
        vol = 0
        while left < right:
            max_left = max(max_left,  height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                vol += max_left - height[left]
                left += 1
            else:
                vol += max_right - height[right]
                right -= 1
        return vol


class Solution2:
    """动态规划
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left = [0] * n
        max_rihgt = [0] * n
        vol = 0
        max_left[0] = height[0]
        max_rihgt[n-1] = height[n-1]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        for j in range(n-2, -1, -1):
            max_rihgt[j] = max(max_rihgt[j+1], height[j])
        for idx in range(n):
            vol += min(max_left[idx], max_rihgt[idx]) - height[idx]
        return vol


class Solution3():
    """栈"""
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: return 0
        stack = []
        vol = 0
        for idx in range(n):
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if not stack: continue
                h = min(height[idx], height[stack[-1]]) - height[top]
                dis = idx - stack[-1] - 1
                vol += h * dis
            stack.append(idx)
        return vol


if __name__ == '__main__':
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    A = Solution3()
    print(A.trap(arr))

