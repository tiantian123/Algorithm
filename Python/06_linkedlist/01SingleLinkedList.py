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
        if node is None: # 如果是空结点，则什么都不做
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
        not_found = False # 如果node没有存在于链表中，则该标量设置为True
        #while pro.next_node != node:


