#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/23 23:39
# @Author: Tian Chen
# @File: 322_Coin_changes.py
"""
322. Change Coins
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        print(dp)
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= amount:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return dp[amount] if dp[amount] <= amount else -1


class Solution2:
    def waysToChange(self, n: int) -> int:
        coin = [25, 10, 5, 1]
        dp = [0] * (n+1)
        dp[0] = 1
        for i in coin:
            for j in range(i, n+1):
               dp[j] += dp[j-i]
        return dp[n] % 1000000007


if __name__ == '__main__':
    arr = [2]
    amount = 3
    A = Solution()
    print(A.coinChange(arr, amount))
    B = Solution2()
    print(B.waysToChange(5))