import copy
import itertools
import random
table = []

def initialize_table():
	soduku_file = open('soduku.txt')
 	file_lines = soduku_file.readlines()
	for line in file_lines:
		line_stripped = line.strip()
		table.append(line_stripped.split(","))
	return

def omit_random_numbers(_tab, it_num):
    tab = copy.deepcopy(_tab)
    all_permutations = list(itertools.product('012345678', repeat=2))
    random.shuffle(all_permutations)
    blank_positions = all_permutations[0:it_num]
    # print len(blank_positions)
    for elem in blank_positions:
        tab[int(elem[0])][int(elem[1])] = '*'
    return tab, blank_positions

class Node:
	def __init__(self, table, blank_positions):
		self.table = table
		self.blank_positions = blank_positions

	def print_table(self):
		for rows in self.table:
			print rows

	def verify_table(self, inserted_num, new_x, new_y):
		for temp_list in self.table: # checking column rule
			if temp_list[new_y] == inserted_num:
				return False
		
		if inserted_num in self.table[new_x]: # checking row rule
			return False
		
		if new_x <= 2: # checking squares rule 
			if new_y <=2:
				for x in xrange(0, 3):
					for y in xrange(0, 3):
						if self.table[x][y] == inserted_num:
							return False
			elif new_y >= 3 and new_y <=5:
				for x in xrange(0, 3):
					for y in xrange(3, 6):
						if self.table[x][y] == inserted_num:
							return False
			elif new_y >= 6:
				for x in xrange(0, 3):
					for y in xrange(6, 9):
						if self.table[x][y] == inserted_num:
							return False
		
		if (new_x >= 3 and new_x <= 5):
			if new_y <=2:
				for x in xrange(3, 6):
					for y in xrange(0, 3):
						if self.table[x][y] == inserted_num:
							return False
			elif (new_y >= 3 and new_y <=5):
				for x in xrange(3, 6):
					for y in xrange(3, 6):
						if self.table[x][y] == inserted_num:
							return False
			elif new_y >= 6:
				for x in xrange(3, 6):
					for y in xrange(6, 9):
						if self.table[x][y] == inserted_num:
							return False
		if new_x >= 6:
			if new_y <=2:
				for x in xrange(6, 9):
					for y in xrange(0, 3):
						if self.table[x][y] == inserted_num:
							return False
			elif (new_y >= 3 and new_y <=5):
				for x in xrange(6, 9):
					for y in xrange(3, 6):
						if self.table[x][y] == inserted_num:
							return False
			elif new_y >= 6:
				for x in xrange(6, 9):
					for y in xrange(6, 9):
						if self.table[x][y] == inserted_num:
							return False
		return True

	# def goal_test(self)
	# 	if ()

initialize_table()
table, blank_positions = omit_random_numbers(table, 40)
node1 = Node(table, blank_positions)
node1.print_table()
while True:
	num = raw_input()
	pos_x = raw_input()
	pos_y = raw_input()
	node1.print_table()
	print node1.verify_table(num, int(pos_x), int(pos_y))
