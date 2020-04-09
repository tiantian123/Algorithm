#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/4/9 20:23
# @Author: Tian Chen
# @File: Day20_208_TireTree.py
"""
208.实现一个Trie树（前缀树）
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
obj.insert('worldhello')
param_2 = obj.search('worldhello')
param_3 = obj.startsWith('wor')
print(param_2,param_3)
