#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/11 20:29
# @Author: Tian Chen
# @File: Day2_RotateAarray.py
"""
189. 旋转数组
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例：
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
说明：
    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。
"""
from typing import List


class Solution:

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        方法一：切片法
        :param nums: 数组
        :param k: 右移单位数
        :return: 修改好的数组
        """
        length = len(nums)
        pos = k % length
        if pos > 0:
            nums[:] = nums[-pos:] + nums[:-pos]
        print("rotate1: ", nums)

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        方法二：翻转法
        """
        k %= len(nums)
        if k != 0:
            nums = nums[::-1] # 第一次翻转，整体翻转
            nums[:k] = nums[:k][::-1] # 第二次翻转，前k个翻转
            nums[k:] = nums[k:][::-1] # 第三次翻转，数组剩余部分翻转
        print("rotate2: ", nums)

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        方法三：环状替换法，遍历数组，给每个值找到其正确的位置，并用tmp作为中间变量存储被替换位置的值。
        注意：在 k% len(nums) != 0时，数组的每个值都需要重新归置一次位置，所以需要cnt来做督导。
        :param nums:
        :param k:
        :return:
        """
        length = len(nums)
        k %= length
        start = 0
        tmp = nums[start]
        cnt = 0
        while cnt < length:
            nxt = (start + k) % length
            while nxt != start:
                nums[nxt], tmp = tmp, nums[nxt]
                nxt = (nxt + k) % length
                cnt += 1
            nums[nxt] = tmp
            start += 1
            tmp = nums[start]
            cnt += 1
        print("rotate3: ", nums)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    k = 3
    Solu = Solution()
   # Solu.rotate3(arr, k)
    Solu.rotate1(arr, k)
   # Solu.rotate2(arr, k)


