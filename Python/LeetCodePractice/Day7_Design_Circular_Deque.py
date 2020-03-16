#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/16 19:32
# @Author: Tian Chen
# @File: Day7_Design_Circular_Deque.py
"""
641. Design Circular Deque
Design your implementation of the circular double-ended queue (deque).
Your implementation should support following operations:
MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not.
isFull(): Checks whether Deque is full or not.
"""


class MyCircularDeque:

    def __init__(self, k):
        self._size = 0
        self._capacity = k
        self._front = 0
        self._tail = 0
        self._data = [-1] * k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :param value: int
        :return: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def insertTail(self, value):
        """
        Adds an item at the tail of Deque. Return true if the operation is successful.
        :param value:
        :return:
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._tail] = value
        else:
            self._tail = (self._tail + 1) % self._capacity
            self._data[self._tail] = value
        self._size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :return:
        """
        if self.isEmpty():
            return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._tail = self._front
        return True

    def deleteTail(self):
        """
        Deletes an item from the tail of Deque. Return true if the operation is successful.
        :return:
        """
        if self.isEmpty():
            return False
        self._data[self._tail] = -1
        self._tail = (self._tail - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._tail
        return True

    def getFront(self):
        """
        Get the front item from the deque
        :return:
        """
        return self._data[self._front]

    def getTail(self):
        """
        Get the last item from the deque
        :return: int
        """
        return self._data[self._tail]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not
        :return: bool
        """
        return self._size == 0

    def isFull(self):
        """
        checks whether the circular deque is full or not
        :return: rtype:bool
        """
        return self._size == self._capacity
