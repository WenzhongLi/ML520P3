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
    def __init__(self, map_matrix, size, disable_print=False):
        self.disable_print = disable_print
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
        # print check
        self.print_believe()

    def print_believe(self):
        if self.disable_print:
            return
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
        type_possibility = [Decimal(0.2), Decimal(0.3), Decimal(0.3), Decimal(0.2)]
        node_map_by_type = dict()
        for i in range(0, 4):
            node_map_by_type[i] = []
        for m in range(0, self.size):
            for n in range(0, self.size):
                node_map_by_type[self.map[m][n]].append((m, n))
        for k in range(self.size):
            self.believe_matrix.append([])
            for j in range(self.size):
                self.believe_matrix[k].append(Decimal(1)/Decimal(self.size*self.size))
        possibility_by_type = [Decimal(0.1), Decimal(0.3), Decimal(0.7), Decimal(0.9)]
        # random a target
        random_for_target = random.choice(range(0, self.size * self.size))
        target = (random_for_target / self.size, random_for_target % self.size)
        self.target = target
        count = 0
        while 1:
            # find a type to update
            max_possibility = Decimal(-1)
            max_possibility_type = -1
            for p in range(0,len(type_possibility)):
                if max_possibility == Decimal(-1):
                    max_possibility = type_possibility[p]*(Decimal(1) - possibility_by_type[p])
                    max_possibility_type = p
                elif max_possibility < type_possibility[p]*(Decimal(1) - possibility_by_type[p]):
                    max_possibility = type_possibility[p]*(Decimal(1) - possibility_by_type[p])
                    max_possibility_type = p
            # update type possibility and normalization
            current_type_possibility = possibility_by_type[max_possibility_type]
            current_node_possibility = type_possibility[max_possibility_type]
            type_possibility[max_possibility_type] = current_type_possibility * current_node_possibility
            normalize_factor = current_type_possibility * current_node_possibility + (1 - current_node_possibility)
            # for p in range(0, len(type_possibility)):
            #     type_possibility[p] = type_possibility[p]/normalize_factor
            #     print_num = copy.copy(type_possibility[p])
            #     print ("%.3f" % print_num.quantize(Decimal('0.00'))),
            # print "\n",

            # check every node is that type

            for current_node in node_map_by_type[max_possibility_type]:
                if current_node == target:
                    if random.random() > possibility_by_type[max_possibility_type]:
                        # bull's-eye
                        print "success", count
                        return count
                    # else:
                        # print "miss"
                count += 1


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    size = 50
    # set the size and density of this matrix
    generator = generater.Generator(size)
    # generator.paint_random()
    # generator.print_matrix()
    # hunter_game = hunter_HCT(generator.get_matrix(), size)
    # print hunter_game.find_target()
    print ('start over')
    count = 0
    for i in range(0, 200):
        if i % 10 == 0:
            print i, count
        generator.paint_random()
        hunter_game = hunter_HCT(generator.get_matrix(), size, True)
        count += hunter_game.find_target()
    print count/200
