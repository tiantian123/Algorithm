#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/11 5:46
# @Author: Tian Chen
# @File: 02LRUCache.py


class DbListNode(object):
    """
    Definition for singly-linked list
    """

    def __init__(self, x, y):
        """
        定义双向链表
        :param x: 密钥
        :param y: 需要写入的数据
        """
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    """
    leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
        当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        # self.top 和 self.tail 作为哨兵结点，避免越界
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:
        """

        :param key:
        :return:
        """
        if key in self.hkeys.keys():
            # 更新结点顺序
            cur = self.hkeys[key]
            # 跳出原来位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 最近使用的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """

        :param key:
        :param value:
        :return:
        """
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            # 跳出原位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # 最近使用的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            # 增加新结点至首部
            cur = DbListNode(key, value)
            self.hkeys[key] = cur #容易出错
            # 最近使用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            # print(self.top.next.val)
            cur.next = top_node
            top_node.prev = cur
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                # 去掉原尾部结点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)
    cache.get(3)
    cache.put(3, 3)
    print(cache)
    cache.get(2)
    cache.put(4, 4)
    print(cache)
    cache.get(1)
    cache.get(3)
    print(cache)
    cache.get(4)
    print(cache)
