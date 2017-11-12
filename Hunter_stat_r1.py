# coding : utf-8
#author : GE

from decimal import *
import sys
import random
import generater

class hunter(object):
    def __init__(self, map, size):
        self.target = (-1,-1)
        self.size = size
        self.map = map
        self.belif = [Decimal(0.2),Decimal(0.3),Decimal(0.3),Decimal(0.2)]

    def find_target(self):
        list = {}
        plane = []
        forest = []
        hill = []
        cave = []
        self.belif = [Decimal(0.2), Decimal(0.3), Decimal(0.3), Decimal(0.2)]
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.map[i][j] == 0:
                    plane.append((i,j))
                if self.map[i][j] == 1:
                    hill.append((i,j))
                if self.map[i][j] == 2:
                    forest.append((i,j))
                if self.map[i][j] == 3:
                    cave.append((i,j))
        list[0] = plane
        list[1] = hill
        list[2] = forest
        list[3] = cave

        # init
        possibility_by_type = [Decimal(0.1), Decimal(0.3), Decimal(0.7), Decimal(0.9)]

        # random a target
        random_for_target = random.choice(range(0, self.size * self.size))
        target = (random_for_target / self.size, random_for_target % self.size)
        self.target = target

        # random a start
        random_x = random.choice(range(0, self.size))
        random_y = random.choice(range(0, self.size))
        first_node = (random_x, random_y)

        count = 1
        current_node = first_node
        current_type = self.map[current_node[0]][current_node[1]]
        while 1:
            current_nodes = list[current_type]

            # check point
            for node in current_nodes:
                if node == target:
                    if random.random() > possibility_by_type[current_type]:
                        # bull's-eye
                        print "success"
                        return count
                    else:
                        print "miss"
                count += 1

            # update belif
            if current_type == 0:
                norm = self.belif[0] * possibility_by_type[0] + (1 - self.belif[0])
                self.belif[0] = self.belif[0] * possibility_by_type[0] / norm
                self.belif[1] = self.belif[1] / norm
                self.belif[2] = self.belif[2] / norm
                self.belif[3] = self.belif[3] / norm

            if current_type == 1:
                norm = self.belif[1] * possibility_by_type[1] + (1 - self.belif[1])
                self.belif[1] = self.belif[1] * possibility_by_type[1] / norm
                self.belif[0] = self.belif[0] / norm
                self.belif[2] = self.belif[2] / norm
                self.belif[3] = self.belif[3] / norm
            if current_type == 2:
                norm = self.belif[2] * possibility_by_type[2] + (1 - self.belif[2])
                self.belif[2] = self.belif[2] * possibility_by_type[2] / norm
                self.belif[1] = self.belif[1] / norm
                self.belif[0] = self.belif[0] / norm
                self.belif[3] = self.belif[3] / norm
            if current_type == 3:
                norm = self.belif[3] * possibility_by_type[3] + (1 - self.belif[3])
                self.belif[3] = self.belif[3] * possibility_by_type[3] / norm
                self.belif[1] = self.belif[1] / norm
                self.belif[2] = self.belif[2] / norm
                self.belif[0] = self.belif[0] / norm

            current_type = self.get_highest_p(self.belif)

    def get_highest_p(self,belif):
        index = -1
        max = -1
        for i in range(0,4):
           if max < belif[i]:
               max = belif[i]
               index = i
        return index


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    size = 50
    # set the size and density of this matrix
    avg = 0;
    for x in range(0, 100):
        generator = generater.Generator(size)
        generator.paint_random()
        generator.print_matrix()
        hunter_game = hunter(generator.get_matrix(), size)
        cur = hunter_game.find_target()
        avg = avg + cur

    print avg / 100
    print ('start over')