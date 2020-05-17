#!/usr/bin/env python
# -** coding: utf-8 -*-
# @Time: 2020/5/17 5:29
# @Author: Tian Chen
# @File: 210_course_schedule.py
from typing import List


class CourseSchedule():
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # 入度表
        in_degree = [0] * numCourses
        # 邻接矩阵
        adj = [set() for _ in range(numCourses)]
        # 初始化
        for a, b in prerequisites:
            in_degree[a] += 1
            adj[b].add(a)
        queue = []
        for node in range(in_degree):
            if in_degree[node] == 0:
                queue.append(node)
        while queue:
            top = queue.pop(0)
            res.append(top)

            for next_node in adj[top]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)
        if len(res) != numCourses:
            return []
        return res