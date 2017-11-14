#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import random
import sys
from decimal import *
import random
import generater_MT
import copy


class hunter_HCT(object):
    # highest probability of containing the target.
    def __init__(self, map_matrix, size, generator, disable_print = False):
        self.disable_print = disable_print
        self.generator = generator
        self.target = (-1, -1)
        self.size = size
        self.map = map_matrix
        self.believe_matrix = []
        for k in range(self.size):
            self.believe_matrix.append([])
            for j in range(self.size):
                self.believe_matrix[k].append(Decimal(1)/Decimal(size*size))

    def normalize(self, normalize_factor):
        # self.print_believe()
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

    def believe_normalize(self):
        self.print_believe()
        normalize_factor = Decimal(0)
        for m in range(self.size):
            for n in range(self.size):
                if self.believe_matrix[m][n] > 0:
                    normalize_factor += self.believe_matrix[m][n]
        check = Decimal(0)
        for m in range(self.size):
            for n in range(self.size):
                if self.believe_matrix[m][n] > 0:
                    self.believe_matrix[m][n] = self.believe_matrix[m][n] / normalize_factor
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
                print_num = copy.copy(self.believe_matrix[m][n]*Decimal(1000))
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

        self.target = self.generator.get_target()
        # random a start
        random_for_first_pick = random.choice(range(0, self.size * self.size))
        first_node = (random_for_first_pick/self.size, random_for_first_pick % self.size)
        count = 1
        current_node = first_node
        last_cross_type = (-1, -1)
        cannot_determine_start_or_end = True
        while 1:
            # check point
            if current_node == self.target:
                current_type = self.map[current_node[0]][current_node[1]]
                if random.random() > possibility_by_type[current_type]:
                    # bull's-eye
                    print "success", count
                    return count
                # else:
                #     print "find fail"
            count += 1
            # update possibility
            current_type = self.map[current_node[0]][current_node[1]]
            current_type_possibility = possibility_by_type[current_type]
            current_node_possibility = self.believe_matrix[current_node[0]][current_node[1]]
            self.believe_matrix[current_node[0]][current_node[1]] = current_type_possibility * current_node_possibility
            normalize_factor = current_type_possibility * current_node_possibility + (1 - current_node_possibility)
            # print normalize_factor
            self.normalize(normalize_factor)
            # get a move
            cross_type = self.generator.get_cross_information()
            self.target = self.generator.get_target()
            # logic determining for start and end
            if cannot_determine_start_or_end:
                if cross_type[1] == cross_type[0]:
                    cannot_determine_start_or_end = False
                elif last_cross_type == (-1, -1):
                    last_cross_type = cross_type
                elif last_cross_type == (cross_type[1], cross_type[0]):
                    last_cross_type = cross_type
                else:
                    cannot_determine_start_or_end = False
            # print cross_type, self.target
            # refactor possibility
            new_believe_matrix = []
            for k in range(self.size):
                new_believe_matrix.append([])
                for j in range(self.size):
                    new_believe_matrix[k].append(Decimal(0))
            direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for m in range(self.size):
                for n in range(self.size):
                    possible_direction_count = 0
                    if self.map[m][n] != cross_type[0]:
                        continue
                    for d in direction:
                        if 0 <= (m + d[0]) < self.size and 0 <= (n + d[1]) < self.size and \
                                        self.map[m + d[0]][n + d[1]] == cross_type[1]:
                            possible_direction_count += 1
                    for d in direction:
                        if 0 <= (m + d[0]) < self.size and 0 <= (n + d[1]) < self.size and \
                                        self.map[m + d[0]][n + d[1]] == cross_type[1]:
                            new_believe_matrix[m + d[0]][n + d[1]] += \
                                self.believe_matrix[m][n]/Decimal(possible_direction_count)
                            #print (m, n), (m + d[0],n + d[1]), self.believe_matrix[m][n], \
                            # Decimal(possible_direction_count), new_believe_matrix[m + d[0]][n + d[1]]

                    # if possible_direction_count != 0:
                    #     print (m,n), possible_direction_count
            if cannot_determine_start_or_end:
                cross_type = (cross_type[1], cross_type[0])
                for m in range(self.size):
                    for n in range(self.size):
                        possible_direction_count = 0
                        if self.map[m][n] != cross_type[0]:
                            continue
                        for d in direction:
                            if 0 <= (m + d[0]) < self.size and 0 <= (n + d[1]) < self.size and \
                                            self.map[m + d[0]][n + d[1]] == cross_type[1]:
                                possible_direction_count += 1
                        for d in direction:
                            if 0 <= (m + d[0]) < self.size and 0 <= (n + d[1]) < self.size and \
                                            self.map[m + d[0]][n + d[1]] == cross_type[1]:
                                new_believe_matrix[m + d[0]][n + d[1]] += \
                                    self.believe_matrix[m][n] / Decimal(possible_direction_count)

            self.believe_matrix = copy.copy(new_believe_matrix)
            self.believe_normalize()

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
    size = 10
    # set the size and density of this matrix
    generator = generater_MT.Generator(size)
    generator.paint_random()
    generator.print_matrix()
    hunter_game = hunter_HCT(generator.get_matrix(), size, generator)
    print hunter_game.find_target()
    print ('start over')
    size = 50
    # set the size and density of this matrix
    generator = generater_MT.Generator(size)
    generator.paint_random()
    generator.print_matrix()
    hunter_game = hunter_HCT(generator.get_matrix(), size, generator, True)
    print hunter_game.find_target()
    count = 0
    for i in range(0, 200):
        if i % 10 == 0:
            print i, count
        generator = generater_MT.Generator(size)
        generator.paint_random()
        hunter_game = hunter_HCT(generator.get_matrix(), size, generator, True)
        count += hunter_game.find_target()
    print count / 200
