from random import randint

table = []

def initialize_table():
    soduku_file = open('soduku.txt')
    file_lines = soduku_file.readlines()
    for line in file_lines:
        line_stripped = line.strip()
        table.append(line_stripped.split(","))
    return


def omit_random_numbers(num_of_omissions): # is to be changed with amin's method!!!
    for i in xrange(num_of_omissions):
        rand_num1 = randint(0, 8)
        rand_num2 = randint(0, 8)
        # print str(rand_num1) + " " + str(rand_num2)
        table[rand_num1][rand_num2] = "*"
    return


class Node:
    def __init__(self, table):
        self.table = table

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
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 3 and new_y <=5:
                for x in xrange(0, 3):
                    for y in xrange(3, 6):
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 6:
                for x in xrange(0, 3):
                    for y in xrange(6, 9):
                        if table[x][y] == inserted_num:
                            return False

        if new_x >= 3 and new_x <= 5:
            if new_y <=2:
                for x in xrange(3, 6):
                    for y in xrange(0, 3):
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 3 and new_y <=5:
                for x in xrange(3, 6):
                    for y in xrange(3, 6):
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 6:
                for x in xrange(3, 6):
                    for y in xrange(6, 9):
                        if table[x][y] == inserted_num:
                            return False
        if new_x >= 6:
            if new_y <=2:
                for x in xrange(6, 9):
                    for y in xrange(0, 3):
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 3 and new_y <=5:
                for x in xrange(6, 9):
                    for y in xrange(3, 6):
                        if table[x][y] == inserted_num:
                            return False
            elif new_y >= 6:
                for x in xrange(6, 9):
                    for y in xrange(6, 9):
                        if table[x][y] == inserted_num:
                            return False
        return True

initialize_table()
omit_random_numbers(40)

n1 = Node(table)
while True:
    num = raw_input()
    pos_x = raw_input()
    pos_y = raw_input()
    n1.print_table()
    print n1.verify_table(num, int(pos_x), int(pos_y))
