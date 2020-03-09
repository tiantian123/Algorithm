#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/8 21:21
# @Author: Tian Chen
# @Function: 单链表的增删查改
# @File: 01SingleLinkedList.py

class Node(object):
    """链表结构的Node结点"""

    def __init__(self, data, next_node=None):
        """
        Node 的初始化方法
        :param data: 存储的数据
        :param next_node: 下一个结点的引用地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """
        结点存储值的获取
        :return: 返回当前节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        结点存储数据的设置方法
        :param data: 新的存储数据
        """
        self.__data = data

    @property
    def next_node(self):
        """
        获取Node指针的值
        :return: next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """
        Node结点next指针的修改方法
        :param next_node: 新的下一个Node结点的引用
        """
        self.__next = next_node


class SingleLinkedList(object):
    """
    单向链表
    """

    def __init__(self):
        """ 单向链表的初始化方法"""
        self.__head = None

    def find_by_value(self, value):
        """
        按值查找
        :param value: 查找的数据
        :return: Node
        """
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index):
        """
        按照索引值在列表中查找
        :param index: 索引值
        :return: node
        """
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def insert_to_head(self, value):
        """
        在链表的头部插入一个存储value数值的结点
        :param value: 将要存储的值
        """
        node = Node(value)
        node.next_node = self.__head
        self.__head = None

    def insert_after(self, node, value):
        """
        在链表的某个指定Node结点之后插入一个存储value数据的Node结点
        :param node: 指定node结点
        :param value: 插入新Node中存储的数据
        """
        if node is None:  # 如果是空结点，则什么都不做
            return
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        """
        在链表指定的某个结点之前插入一个存储value数据的结点
        :param node:  某结点
        :param value: 插入结点存储的数据
        """
        if (node is None) or (self.__head is None):
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False  # 如果node没有存在于链表中，则该标量设置为True
        while pro.next_node != node:
            if pro.next_node is None:
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def delete_by_value(self, value):
        """
        在链表中删除指定存储数据的Node结点
        :param value: 要删除结点的存储数据
        """
        if self.__head is None:
            return
        if self.__head.data == value:
            self.__head = self.__head.next_node

        pro = self.__head
        node = self.__head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:
                not_found = True
                return
            else:
                pro = node
                node = node.next_node
        if not_found is False:
            pro.next_node = node.next_node

    def delete_by_node(self, node):
        """
        在链表中删除指定结点
        :param node: 需要删除的结点
        """
        if self.__head is None:
            return

        if node == self.__head:
            self.__head = node.next_node
            return

        pro = self.__head
        not_found = False
        while pro.next_node != node:
            if pro.next_node is None:
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_last_n_node(self, n):
        """
        删除链表中倒数第N个结点
        主体思路：设置快慢指针，快指针先行n步，之后再快慢指针同时移动。当快指针到达链表尾部时，
        删除慢指针指向的链表结点
        :param n: 需要删除的倒数第n个结点
        """
        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            tmp = slow
            fast = fast.next_node
            slow = slow.next_node

        tmp.next_node = slow.next_node

    def find_mid_node(self):
        """
        查找链表中的中间结点
        主体思路：快慢指针，快指针每次跨2步，慢指针跨一步，快指针到链表尾部时，慢指针指向链表中间结点
        :return: 链表的中间结点
        """
        fast = self.__head
        slow = self.__head
        # 疑问： 如果链表长度是奇数呢？fast最后跨的2步会不会报错
        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow

    def create_node(self, value):
        """
        创建一个存储value值得结点
        :param value: 将要存储在node中的数据
        :return: 新结点
        """
        return Node(value)

    def print_all(self):
        """
        打印当前链表的所有结点
        """
        pos = self.__head
        if pos is None:
            print("当前链表为空")
            return
        while pos.next_node is not None:
            print(str(pos.data) + "-->", end="")
            pos = pos.next_node
        print(str(pos.data))

    def reversed_self(self):
        """
        链表翻转
        """
        if self.__head is None or self.__head.next_node is None:
            return

        pre = self.__head
        node = self.__head.next_node
        while node is not None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self.__head.next_node = None
        self.__head = pre

    def __reversed_with_two_node(self, pre, node):
        """
        翻转相邻的两个结点
        :param pre: 前结点
        :param node: 后结点
        :return: 下一个相邻结点的元组
        """
        tmp = node.next_node
        node.next_node = pre
        pre = node
        node = tmp
        return pre, node

    def has_ring(self):
        """
        检查链表中是否有环
        主体思想：快慢指针，快指针每次2步，慢指针1步，如果快慢指针没有相遇，而是顺利达到链表尾部，
        说明没有环，否则存在环。
        :return: True-有环，False-无环
        """
        fast = self.__head
        slow = self.__head

        while (fast.next_node is not None) and (fast is not None):
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True

        return False
