#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/3/14 4:39
# @Author: Tian Chen
# @File: 03.palindrome.py

import sys
sys.path.append('01SingleLinkedList')
from 01SingleLinkedList import SingleLinkedList

def reverse(head):
    reverse_head = None
    while head:
        next = head._next
        head._next = reverse_head
        reverse_head = head
        head = next
    return reverse_head

def is_palindrome():
