#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/29 12:02
# @Author: Tian Chen
# @File: Day15_122_BuySellStock.py
"""
122. Best Time to buy and sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit