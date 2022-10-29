#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 29/10/2022 下午6:22
# @Author  : brUce 杨
# @File    : 列表基础操作.py.py

"""列表基础操作"""
list1 = [0, 2, 56, 4, 9, 17, 30, 7, 8, 2]
# 第零.将列表元素翻转
list_turn = list1[::-1]
print(list_turn)
# 第一.让列表数字从小到大排序
list1.sort()
print(list1)
# 第二.让列表数字从大到小排序
list1.sort(reverse=True)
print(list1)
# 第三.将列表去重
list_only = set(list1)
print(list_only)
# 第四.将列表求和
list_total = sum(list1)
print(list_total)
# 第五.取列表前五个数
list_five = list1[0:5]
print(list_five)
# 第六.取列表最大值
list_max = max(list1)
print(list_max)
# 第七.将列表转换为字符串,用空格隔开
list_str = " ".join(str(x) for x in list1)
print(list_str)
# 第八.将列表数字转换为字符串
list1_str = [str(x) for x in list1]
print(list1_str)
# 第九.在列表头部插入0
list1.insert(0, 0)
print(list1)
# 第十.删除列表第一个元素
del(list1[0])
print(list1)
