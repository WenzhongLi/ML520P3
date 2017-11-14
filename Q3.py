#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import generater
import Hunter_part1_HCT
import Hunter_part1_HFT
import random

count_rule1 = [0,0,0,0]
count_rule2 = [0,0,0,0]
count_rule1_diff_map = [0,0,0,0]
count_rule2_diff_map = [0,0,0,0]
size = 50
test_num = 1000
generator = generater.Generator(size)
matrix = generator.get_matrix()
node_map_by_type =dict()
for i in range(0, 4):
    node_map_by_type[i] = []
for m in range(0, size):
    for n in range(0, size):
        node_map_by_type[matrix[m][n]].append((m, n))
for type in range(0, 4):
    for i in range(0,test_num):
        if i % 100 == 0:
            print "i", i
        target_node = random.choice(node_map_by_type[type])
        hunter_rule1 = Hunter_part1_HCT.hunter_HCT(matrix, size, True)
        count_rule1[type] += hunter_rule1.find_target(target_node)

        hunter_rule2 = Hunter_part1_HFT.hunter_HCT(matrix, size, True)
        count_rule2[type] += hunter_rule2.find_target(target_node)
for type in range(0, 4):
    for i in range(0, test_num):
        if i % 100 == 0:
            print "i", i
        generator = generater.Generator(size)
        generator.paint_random()
        matrix = generator.get_matrix()
        for i in range(0, 4):
            node_map_by_type[i] = []
        for m in range(0, size):
            for n in range(0, size):
                node_map_by_type[matrix[m][n]].append((m, n))
        target_node = random.choice(node_map_by_type[type])
        hunter_rule1 = Hunter_part1_HCT.hunter_HCT(generator.get_matrix(), size, True)
        count_rule1_diff_map[type] += hunter_rule1.find_target(target_node)

        hunter_rule2 = Hunter_part1_HFT.hunter_HCT(generator.get_matrix(), size, True)
        count_rule2_diff_map[type] += hunter_rule2.find_target(target_node)

print "count_rule1", count_rule1,
for i in range(0,4):
    print count_rule1[i]/test_num,
print "\n",
print "count_rule2", count_rule2,
for i in range(0,4):
    print count_rule2[i]/test_num,
print "\n",
print "count_rule1_diff_map", count_rule1_diff_map,
for i in range(0,4):
    print count_rule1_diff_map[i]/test_num,
print "\n",
print "count_rule2_diff_map", count_rule2_diff_map,
for i in range(0,4):
    print count_rule2_diff_map[i]/test_num,
print "\n",
