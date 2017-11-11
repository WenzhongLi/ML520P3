#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import random
import sys
from decimal import *
import random
import generater
import copy


class hunter_HCT(object):
    # highest probability of containing the target.
    def __init__(self, map_matrix, size):
        self.target = (-1, -1)
        self.size = size
        self.map = map_matrix
        self.believe_matrix = []
        for k in range(self.size):
            self.believe_matrix.append([])
            for j in range(self.size):
                self.believe_matrix[k].append(Decimal(1)/Decimal(size*size))

    def normalize(self, normalize_factor):
        self.print_believe()
        # for m in range(self.size):
        #     for n in range(self.size):
        #         if self.believe_matrix[m][n] > 0:
        #             normalize_factor += self.believe_matrix[m][n]
        check = Decimal(0)
        for m in range(self.size):
            for n in range(self.size):
                if self.believe_matrix[m][n] > 0:
                    self.believe_matrix[m][n] = self.believe_matrix[m][n]/normalize_factor
                    check += self.believe_matrix[m][n]
        print check
        self.print_believe()

    def print_believe(self):
        for m in range(self.size):
            for n in range(self.size):
                if (m, n) == self.target:
                    sf = '\033[1;35m\033[0m'
                else:
                    sf = '\033[0m'
                print_num = self.believe_matrix[m][n]*Decimal(1000)
                print (sf+"%.3f" % print_num.quantize(Decimal('0.00'))),
            print "\n",
        print "\n",

    def find_target(self):
        # init
        for k in range(self.size):
            self.believe_matrix.append([])
            for j in range(self.size):
                self.believe_matrix[k].append(Decimal(1)/Decimal(self.size*self.size))
        possibility_by_type = [Decimal(0.1), Decimal(0.3), Decimal(0.7), Decimal(0.9)]
        # random a target
        random_for_target = random.choice(range(0, self.size * self.size))
        target = (random_for_target / self.size, random_for_target % self.size)
        self.target = target
        # random a start
        random_for_first_pick = random.choice(range(0,self.size * self.size))
        first_node = (random_for_first_pick/self.size, random_for_first_pick % self.size)
        count = 1
        current_node = first_node
        while 1:
            # check point
            if current_node == target:
                current_type = self.map[current_node[0]][current_node[1]]
                if random.random() > possibility_by_type[current_type]:
                    # bull's-eye
                    print "success"
                    return count
            count += 1
            # update possibility
            current_type = self.map[current_node[0]][current_node[1]]
            current_type_possibility = possibility_by_type[current_type]
            current_node_possibility = self.believe_matrix[current_node[0]][current_node[1]]
            self.believe_matrix[current_node[0]][current_node[1]] = current_type_possibility * current_node_possibility
            normalize_factor = current_type_possibility * current_node_possibility + (1 - current_node_possibility)
            print normalize_factor
            self.normalize(normalize_factor)
            # find current highest
            highest_possibility = Decimal(-1)
            highest_possibility_index = (-1, -1)
            for m in range(self.size):
                for n in range(self.size):
                    if highest_possibility == Decimal(-1):
                        highest_possibility = self.believe_matrix[m][n]
                        highest_possibility_index = (m, n)
                    elif highest_possibility < self.believe_matrix[m][n]:
                        highest_possibility = self.believe_matrix[m][n]
                        highest_possibility_index = (m, n)
            current_node = highest_possibility_index


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    size = 5
    # set the size and density of this matrix
    generator = generater.Generator(size)
    generator.paint_random()
    generator.print_matrix()
    hunter_game = hunter_HCT(generator.get_matrix(), size)
    print hunter_game.find_target()
    print ('start over')