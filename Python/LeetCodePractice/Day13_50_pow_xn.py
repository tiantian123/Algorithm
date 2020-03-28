#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/29 0:16
# @Author: Tian Chen
# @File: Day13_50_pow_xn.py
"""
50. 求pow(x,n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)