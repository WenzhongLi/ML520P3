#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import random
import sys
import copy


class Generator(object):
    # init size and density of map
    def __init__(self, size):
        self.size = size
        self.target = (random.choice(range(0, self.size)), random.choice(range(0, self.size)))
        self.map_matrix = []
        for k in range(self.size):
            self.map_matrix.append([])
            for j in range(self.size):
                self.map_matrix[k].append(0)
        self.map_matrix = [[1, 2, 1, 2, 3, 2, 2, 2, 2, 3, 0, 3, 1, 2, 2, 1, 2, 2, 2, 3, 3, 2, 2, 2, 0, 1, 0, 1, 0, 2, 3, 2, 1, 0, 2, 2, 3, 0, 1, 3, 1, 2, 3, 2, 1, 2, 2, 1, 3, 1],
            [0, 3, 3, 2, 2, 3, 2, 1, 0, 1, 2, 2, 0, 2, 1, 1, 3, 2, 3, 2, 2, 3, 0, 2, 2, 1, 3, 0, 2, 0, 1, 1, 1, 1, 3, 1, 1, 3, 2, 1, 0, 3, 1, 2, 0, 0, 3, 0, 0, 2],
            [1, 3, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 2, 3, 1, 2, 2, 0, 3, 0, 2, 1, 3, 1, 3, 1, 2, 1, 0, 1, 2, 1, 2, 3, 1, 3, 0, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 0, 3, 3],
            [0, 0, 2, 2, 2, 2, 2, 3, 3, 1, 1, 3, 0, 1, 1, 2, 3, 3, 2, 1, 3, 2, 1, 0, 1, 2, 1, 0, 2, 2, 3, 0, 0, 0, 3, 0, 3, 3, 1, 3, 2, 3, 2, 3, 2, 2, 2, 0, 3, 3],
            [1, 0, 1, 2, 3, 1, 0, 1, 2, 0, 1, 3, 1, 2, 2, 2, 1, 2, 2, 2, 0, 2, 1, 2, 1, 3, 2, 2, 3, 3, 3, 0, 0, 2, 2, 1, 2, 1, 1, 1, 3, 0, 3, 2, 2, 2, 0, 2, 0, 0],
            [3, 3, 3, 3, 2, 3, 0, 1, 1, 3, 2, 3, 1, 1, 1, 1, 3, 1, 3, 0, 1, 1, 2, 1, 0, 1, 0, 1, 1, 1, 2, 3, 2, 2, 0, 2, 1, 1, 3, 2, 3, 1, 1, 1, 1, 3, 2, 0, 2, 0],
            [3, 2, 1, 2, 3, 1, 2, 0, 2, 3, 3, 1, 0, 3, 2, 3, 1, 1, 1, 2, 2, 0, 2, 2, 3, 0, 1, 2, 0, 1, 3, 2, 0, 0, 2, 3, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 0, 3, 2, 1],
            [2, 1, 1, 2, 2, 0, 3, 2, 1, 0, 2, 2, 0, 0, 0, 1, 1, 0, 1, 0, 0, 2, 3, 0, 3, 0, 1, 0, 0, 3, 3, 1, 0, 1, 1, 1, 2, 1, 0, 0, 2, 1, 2, 1, 2, 2, 1, 3, 3, 1],
            [1, 3, 1, 0, 2, 1, 3, 2, 1, 0, 0, 3, 1, 1, 1, 2, 3, 1, 3, 0, 1, 0, 0, 3, 2, 1, 0, 0, 0, 0, 1, 0, 3, 2, 2, 0, 3, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 0],
            [2, 3, 0, 1, 0, 3, 0, 2, 0, 3, 1, 3, 0, 3, 1, 1, 2, 0, 0, 3, 3, 3, 2, 3, 0, 2, 2, 0, 3, 2, 0, 3, 1, 1, 2, 3, 3, 3, 2, 1, 1, 2, 2, 1, 0, 2, 2, 3, 1, 1],
            [1, 3, 3, 0, 0, 2, 2, 1, 2, 2, 3, 3, 2, 0, 0, 3, 2, 2, 1, 3, 1, 2, 3, 3, 0, 1, 2, 3, 0, 1, 2, 0, 3, 1, 1, 0, 2, 1, 2, 1, 3, 0, 1, 2, 1, 1, 2, 0, 1, 2],
            [2, 3, 2, 1, 0, 3, 1, 0, 2, 1, 1, 2, 0, 2, 1, 2, 3, 2, 0, 3, 3, 3, 2, 2, 1, 2, 0, 2, 1, 2, 1, 2, 1, 1, 3, 1, 3, 0, 0, 2, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1],
            [1, 1, 2, 1, 3, 3, 3, 2, 1, 1, 1, 2, 0, 0, 3, 0, 1, 0, 2, 1, 3, 1, 2, 0, 2, 0, 2, 3, 3, 1, 3, 2, 0, 1, 2, 2, 0, 0, 2, 1, 0, 2, 1, 1, 2, 2, 3, 0, 1, 2],
            [1, 2, 1, 1, 2, 1, 2, 3, 0, 1, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 3, 1, 3, 2, 2, 1, 1, 1, 0, 1, 1, 0, 2, 1, 0, 0, 2, 0, 2, 2, 2, 0, 1, 3, 1, 3, 0, 2, 1, 1],
            [3, 2, 1, 2, 2, 2, 3, 2, 3, 2, 1, 1, 1, 1, 1, 3, 2, 3, 3, 3, 2, 3, 2, 2, 0, 0, 2, 2, 1, 1, 1, 3, 1, 3, 3, 1, 2, 2, 1, 1, 1, 2, 2, 3, 2, 2, 2, 3, 1, 2],
            [1, 2, 0, 3, 1, 1, 2, 1, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 3, 1, 0, 1, 2, 1, 0, 2, 1, 0, 1, 0, 3, 0, 1, 1, 0, 2, 3, 3, 1, 1, 0, 0, 2],
            [3, 0, 2, 3, 3, 1, 3, 3, 1, 1, 2, 1, 2, 2, 3, 0, 3, 3, 1, 2, 0, 0, 0, 2, 1, 1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 0, 3, 2, 1, 0, 0, 2, 0, 2, 1, 1, 1, 0, 2, 0],
            [2, 1, 3, 0, 2, 2, 0, 3, 3, 0, 3, 2, 0, 0, 3, 2, 0, 2, 0, 2, 0, 3, 3, 1, 3, 3, 2, 0, 1, 1, 2, 0, 2, 1, 1, 3, 3, 1, 1, 1, 2, 1, 0, 3, 3, 2, 3, 2, 3, 3],
            [2, 3, 0, 1, 1, 1, 0, 1, 0, 2, 0, 0, 2, 3, 2, 1, 0, 0, 3, 2, 1, 0, 3, 1, 3, 1, 1, 0, 3, 2, 2, 2, 0, 2, 2, 3, 3, 3, 2, 3, 1, 1, 2, 1, 2, 1, 2, 1, 3, 2],
            [1, 2, 2, 0, 3, 2, 2, 3, 2, 1, 2, 2, 1, 2, 0, 1, 1, 1, 3, 1, 1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 3, 0, 2, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 3, 0, 1, 1, 1, 3, 1],
            [1, 1, 2, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 3, 0, 2, 0, 2, 3, 2, 2, 3, 1, 3, 2, 0, 0, 1, 2, 1, 1, 2, 1, 3, 0, 1, 0, 2, 1, 2, 3, 2, 2, 2, 1, 2, 0, 2, 2, 0],
            [2, 1, 3, 2, 2, 2, 1, 3, 2, 3, 0, 0, 3, 1, 2, 3, 2, 0, 1, 1, 1, 2, 0, 1, 0, 3, 0, 2, 3, 3, 3, 0, 1, 3, 2, 2, 2, 2, 2, 3, 1, 1, 1, 3, 1, 2, 3, 2, 2, 2],
            [2, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 3, 2, 2, 1, 0, 1, 2, 1, 2, 1, 3, 0, 2, 3, 2, 2, 3, 3, 1, 2, 3, 2, 3, 1, 1, 1, 2, 3, 0, 0, 1, 2, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 3, 2, 0, 1, 1, 3, 1, 0, 1, 2, 2, 0, 1, 1, 0, 2, 2, 3, 2, 1, 2, 2, 1, 2, 0, 3, 2, 3, 1, 0, 1, 0, 0, 2, 1, 2, 3, 3, 1, 1, 2],
            [2, 0, 0, 1, 0, 3, 0, 1, 1, 3, 0, 3, 3, 0, 3, 1, 2, 3, 3, 0, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 0, 1, 3, 3, 2, 2, 0, 2, 0, 0, 1, 2, 0, 1, 3, 0, 2, 1],
            [3, 3, 1, 0, 2, 2, 0, 3, 3, 3, 1, 1, 1, 1, 2, 1, 2, 0, 2, 3, 2, 0, 2, 2, 2, 0, 1, 0, 1, 1, 2, 0, 0, 2, 2, 3, 0, 1, 1, 3, 2, 1, 1, 1, 0, 0, 2, 0, 1, 1],
            [1, 3, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3, 3, 0, 1, 1, 1, 2, 0, 1, 2, 3, 1, 3, 3, 3, 2, 2, 2, 0, 2, 0, 1, 3, 0, 2, 1, 0, 2, 2, 2, 3, 2, 2, 0, 2],
            [0, 2, 3, 1, 2, 0, 0, 3, 1, 0, 3, 0, 0, 2, 2, 2, 0, 1, 1, 2, 2, 1, 1, 3, 2, 1, 3, 3, 3, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 3, 0, 1, 1, 3, 1, 3, 1, 3, 3],
            [1, 2, 1, 3, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 3, 1, 2, 2, 0, 1, 0, 0, 0, 0, 1, 2, 1, 2, 1, 1, 3, 2, 2, 3, 0, 2, 3, 1, 3, 0, 0, 0, 0, 3, 1, 1, 1],
            [2, 3, 1, 3, 1, 2, 1, 3, 1, 1, 1, 2, 0, 1, 3, 2, 3, 1, 2, 0, 1, 2, 3, 1, 1, 1, 1, 2, 2, 0, 3, 0, 0, 0, 3, 2, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 2, 0, 0, 3],
            [0, 3, 1, 2, 2, 3, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 1, 3, 0, 0, 2, 0, 1, 1, 0, 1, 0, 1, 0, 3, 0, 3, 0, 1, 1, 3, 1, 2, 3, 2, 3, 2, 2, 1, 2],
            [1, 2, 2, 0, 0, 2, 3, 3, 3, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 3, 0, 0, 1, 2, 1, 3, 2, 1, 3, 1, 3, 0, 1, 2, 2, 3, 2, 3, 0, 3, 1, 1, 0, 0, 3, 0, 2, 3, 2, 2],
            [3, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2, 3, 3, 1, 3, 2, 1, 3, 2, 1, 1, 0, 0, 2, 1, 1, 1, 2, 2, 2, 3, 2, 2, 2, 1, 3, 0, 3, 1, 2, 3, 1, 2, 1, 2, 0, 1, 2, 2],
            [1, 1, 1, 3, 0, 1, 2, 2, 0, 0, 2, 3, 1, 2, 1, 2, 0, 0, 0, 3, 3, 0, 2, 0, 1, 1, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 1, 2, 3, 3, 2, 2],
            [3, 3, 0, 0, 2, 3, 0, 3, 1, 1, 3, 2, 3, 1, 1, 0, 3, 2, 3, 1, 2, 1, 1, 1, 3, 1, 2, 3, 1, 0, 2, 3, 0, 0, 2, 1, 2, 3, 1, 3, 2, 2, 0, 1, 2, 1, 1, 1, 2, 1],
            [2, 3, 3, 3, 0, 2, 0, 2, 1, 2, 2, 0, 2, 0, 3, 2, 1, 2, 1, 2, 3, 1, 2, 2, 1, 0, 0, 2, 3, 2, 2, 2, 0, 0, 2, 1, 2, 0, 2, 1, 1, 3, 2, 2, 3, 1, 1, 0, 2, 1],
            [0, 3, 1, 1, 1, 3, 1, 3, 2, 2, 3, 0, 2, 0, 1, 0, 2, 0, 1, 3, 2, 2, 1, 2, 0, 3, 2, 1, 3, 1, 0, 2, 1, 1, 0, 0, 2, 2, 3, 3, 1, 1, 3, 1, 0, 1, 0, 2, 3, 2],
            [2, 2, 3, 1, 0, 0, 0, 1, 0, 0, 0, 3, 2, 1, 1, 1, 1, 2, 2, 1, 2, 3, 1, 0, 0, 0, 2, 2, 0, 0, 0, 3, 2, 2, 2, 1, 0, 3, 1, 2, 1, 0, 2, 3, 0, 0, 3, 2, 2, 3],
            [0, 1, 0, 2, 2, 2, 1, 2, 3, 0, 3, 2, 1, 1, 2, 2, 0, 0, 3, 3, 2, 2, 3, 2, 1, 0, 3, 2, 2, 3, 1, 2, 1, 3, 1, 1, 2, 0, 3, 0, 0, 2, 0, 2, 0, 3, 0, 1, 2, 0],
            [2, 2, 1, 3, 1, 1, 0, 3, 1, 2, 2, 2, 2, 2, 0, 2, 0, 1, 1, 1, 0, 2, 3, 0, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 3, 0, 3, 2, 3, 2, 3, 2, 1, 1, 1, 0, 2, 1, 2, 1],
            [0, 3, 0, 3, 1, 0, 3, 2, 0, 1, 0, 1, 1, 1, 2, 1, 1, 3, 3, 2, 2, 3, 1, 1, 2, 2, 2, 1, 2, 1, 3, 3, 0, 2, 1, 1, 2, 0, 1, 2, 0, 1, 1, 3, 3, 1, 2, 1, 2, 2],
            [1, 1, 0, 1, 2, 2, 3, 1, 1, 2, 3, 3, 1, 2, 0, 3, 0, 2, 1, 3, 3, 3, 1, 1, 3, 0, 0, 1, 2, 2, 2, 0, 1, 2, 3, 3, 0, 2, 1, 3, 1, 2, 3, 2, 1, 1, 1, 0, 2, 0],
            [2, 3, 2, 3, 1, 3, 3, 3, 0, 1, 1, 1, 0, 2, 1, 1, 2, 2, 1, 2, 3, 0, 1, 0, 3, 1, 1, 3, 0, 1, 0, 1, 2, 1, 3, 1, 3, 2, 2, 2, 3, 1, 2, 1, 3, 1, 2, 2, 1, 2],
            [2, 2, 0, 1, 3, 3, 1, 0, 0, 1, 3, 1, 3, 2, 1, 2, 2, 3, 2, 0, 2, 2, 0, 2, 3, 3, 2, 2, 2, 0, 2, 0, 0, 2, 0, 3, 0, 0, 2, 0, 2, 3, 3, 2, 1, 2, 1, 1, 2, 2],
            [3, 2, 0, 2, 1, 1, 0, 1, 0, 1, 2, 3, 1, 0, 0, 2, 1, 1, 3, 1, 2, 0, 0, 2, 2, 3, 1, 1, 1, 1, 0, 3, 2, 3, 3, 1, 1, 3, 1, 1, 1, 0, 2, 1, 0, 2, 3, 2, 2, 2],
            [1, 0, 3, 2, 3, 3, 1, 0, 2, 2, 1, 0, 3, 2, 1, 0, 1, 3, 2, 0, 1, 0, 0, 1, 3, 2, 1, 1, 0, 3, 1, 1, 0, 1, 2, 2, 3, 2, 1, 2, 2, 3, 2, 2, 1, 3, 2, 3, 0, 2],
            [1, 1, 2, 0, 3, 0, 3, 1, 0, 2, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 3, 2, 3, 1, 2, 1, 3, 2, 3, 3, 0, 1, 2, 1, 2, 1, 3, 2, 2, 0, 2, 3, 2, 3, 2, 3],
            [1, 2, 0, 1, 1, 1, 3, 1, 1, 3, 3, 0, 0, 3, 1, 3, 3, 0, 1, 1, 3, 2, 3, 3, 0, 2, 1, 1, 2, 0, 0, 1, 3, 0, 3, 1, 2, 1, 1, 2, 0, 0, 0, 3, 2, 0, 1, 1, 2, 3],
            [0, 0, 1, 2, 3, 2, 1, 0, 1, 1, 0, 2, 3, 3, 3, 1, 3, 3, 0, 2, 3, 1, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0, 2, 1, 2, 0, 2, 1, 3, 0, 0, 3, 2, 2, 0, 0, 2, 2, 3, 3],
            [0, 2, 1, 2, 3, 0, 2, 1, 1, 3, 3, 1, 2, 2, 1, 2, 2, 3, 0, 2, 0, 1, 3, 2, 1, 1, 1, 2, 0, 3, 0, 1, 2, 1, 0, 2, 0, 1, 0, 3, 3, 2, 2, 2, 2, 3, 0, 3, 3, 1],]

    # print map to commend line
    def print_matrix(self):
        count_flat = 0
        count_hill = 0
        count_forest = 0
        count_cave = 0
        # for k in range(self.height):
        #     for j in range(self.width):
        #         print(self.map_matrix[k][j]),
        #     print('\n'),
        for k in range(self.size):
            for j in range(self.size):
                if self.map_matrix[k][j] == 0:
                    print 'p',#plane
                    count_flat += 1
                elif self.map_matrix[k][j] == 1:
                    print 'h',
                    count_hill += 1
                elif self.map_matrix[k][j] == 2:
                    print 'f',
                    count_forest += 1
                elif self.map_matrix[k][j] == 3:
                    print 'c',
                    count_cave += 1
                else:
                    print(self.map_matrix[k][j]),
            print('\n'),
        print(str(count_flat)+" are flat\n")
        print(str(count_hill) + " are hill\n")
        print(str(count_forest) + " are forest\n")
        print(str(count_cave) + " are cave\n")

    # paint maze randomly
    def paint_random(self):
        self.target = (random.choice(range(0, self.size)), random.choice(range(0, self.size)))
        matrix = [[0 for j in range(self.size)] for k in range(self.size)]
        node_list = []
        # init a set of all point could be block
        for k in range(self.size):
            for j in range(self.size):
                node_list.append((k, j))
        hill_forest_cave = int(self.size * self.size * 0.8)
        forest_cave = int(self.size * self.size * 0.5)
        cave = int(self.size * self.size * 0.2)
        # get hill_forest_cave randomly
        hill_forest_cave_set = random.sample(node_list, hill_forest_cave)
        # Paint them 1
        for node in hill_forest_cave_set:
            matrix[node[0]][node[1]] = 1  # means hill_forest_cave
        # get forest_cave point randomly
        forest_cave_set = random.sample(hill_forest_cave_set, forest_cave)
        for node in forest_cave_set:
            matrix[node[0]][node[1]] = 2  # means forest_cave
        # get cave point randomly
        cave_set = random.sample(forest_cave_set, cave)
        for node in cave_set:
            matrix[node[0]][node[1]] = 3  # means forest_cave
        self.map_matrix = matrix
        #self.print_matrix()
        return matrix

    def get_matrix(self):
        return self.map_matrix

    def get_cross_information(self):
        if self.target == (-1, -1):
            print "error"
            return None
        else:
            D_list = [(self.target[0]+1, self.target[1]), (self.target[0], self.target[1]+1),
                      (self.target[0]-1, self.target[1]), (self.target[0], self.target[1]-1)]
            for node in copy.copy(D_list):
                if node[0] < 0 or node[1] < 0 or node[0] >= self.size or node[1] >= self.size:
                    D_list.remove(node)
            move = random.choice(D_list)
            result = (self.map_matrix[self.target[0]][self.target[1]], self.map_matrix[move[0]][move[1]])
            self.target = move
            return result

    def get_target(self):
        return self.target


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    generator = Generator()
    generator.print_matrix()
    generator.paint_random()
    generator.print_matrix()
    print generator.get_cross_information()
    print generator.get_cross_information()
    print generator.get_target((1, 1))
    print generator.get_target(generator.target)
    print ('start over')
