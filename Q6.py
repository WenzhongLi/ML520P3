import generater_MT
import Hunter_part2_HCT
import Hunter_part2_HFT
import random

count_rule1 = 0
count_rule2 = 0
count_rule1_diff_map = 0
count_rule2_diff_map = 0
size = 50
test_num = 1000
generator = generater_MT.Generator(size)
matrix = generator.get_matrix()
node_map_by_type =dict()
for i in range(0, 4):
    node_map_by_type[i] = []
for m in range(0, size):
    for n in range(0, size):
        node_map_by_type[matrix[m][n]].append((m, n))

for i in range(0,test_num):
    if i % 100 == 0:
        print "i", i
    generator = generater_MT.Generator(size)
    hunter_rule1 = Hunter_part2_HCT.hunter_HCT(generator.get_matrix(), size, generator, True)
    count_rule1 += hunter_rule1.find_target()

    generator = generater_MT.Generator(size)
    hunter_rule2 = Hunter_part2_HFT.hunter_HCT(generator.get_matrix(), size, generator, True)
    count_rule2 += hunter_rule2.find_target()

for i in range(0, test_num):
    if i % 100 == 0:
        print "i", i
    generator = generater_MT.Generator(size)
    generator.paint_random()
    hunter_rule1 = Hunter_part2_HCT.hunter_HCT(generator.get_matrix(), size, generator, True)
    count_rule1_diff_map += hunter_rule1.find_target()

    generator = generater_MT.Generator(size)
    generator.paint_random()
    hunter_rule2 = Hunter_part2_HCT.hunter_HCT(generator.get_matrix(), size, generator, True)
    count_rule2_diff_map += hunter_rule2.find_target()

print "count_rule1", count_rule1, count_rule1/test_num

print "count_rule2", count_rule2, count_rule2/test_num

print "count_rule1_diff_map", count_rule1_diff_map, count_rule1_diff_map/test_num

print "count_rule2_diff_map", count_rule2_diff_map, count_rule2_diff_map/test_num
