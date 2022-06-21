"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q1
Date due: 2022-06-21
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


def initialize_world(in_filepath):
    try:
        file = open(in_filepath, 'r')
    except FileNotFoundError:
        return []
    row_list = [line.strip() for line in file]
    file.close()
    return row_list


def count_neighbors(world, position):
    current_row = position[0]
    current_column = position[1]
    neighbor_list_f = []
    for row_range in range(-1, 2):
        for column_range in range(-1, 2):
            if not (column_range == 0 and row_range == 0):

                if current_row == 0:
                    if current_column == 0:
                        if row_range > -1 and column_range > -1:
                            neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                    else:
                        if row_range > -1:
                            try:
                                neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                            except IndexError:
                                continue

                elif current_row == len(world) - 1:
                    if current_column == 0:
                        if row_range < 1 and column_range > -1:
                            neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                    else:
                        if row_range < 1:
                            try:
                                neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                            except IndexError:
                                continue

                else:
                    if current_column == 0:
                        if column_range > -1:
                            neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                    else:
                        try:
                            neighbor_list_f.append(world[current_row + row_range][current_column + column_range])
                        except IndexError:
                            continue

    # print(neighbor_list_f)

    living_neighbors = 0
    for item in neighbor_list_f:
        if item == "*":
            living_neighbors += 1

    return living_neighbors


""" try:
     neighbor_list_above = [world[position[0] - 1][position[1] - 1], world[position[0] - 1][position[1]],
                            world[position[0] - 1][position[1] + 1]]
     neighbor_list_next_to = [world[position[0]][position[1] - 1], world[position[0]][position[1] + 1]]
     neighbor_list_below = [world[position[0] + 1][position[1] - 1], world[position[0] + 1][position[1]],
                            world[position[0] + 1][position[1] + 1]]
     neighbor_list = neighbor_list_above + neighbor_list_next_to + neighbor_list_below"""


def compute_next_generation(start_gen):
    # call count_neighbors in here
    # dashes are dead, asterisks are alive
    new_gen = []
    for row in range(len(start_gen)):
        new_row = ''
        current_row = start_gen[row]
        for column in range(len(current_row)):
            num_living = count_neighbors(start_gen, (row, column))
            if current_row[column] == "*":
                if num_living < 2:
                    new_row += '-'
                elif num_living > 3:
                    new_row += '-'
                else:
                    new_row += '*'
            elif current_row[column] == "-":
                if num_living == 3:
                    new_row += '*'
                else:
                    new_row += '-'
        new_gen.append(new_row)

    return new_gen


def display_world(world):
    # print representation of world to the screen, looks like input file
    for row in world:
        print(row)


def main():
    # print original and then 10 generations after
    first_world = initialize_world("life.txt")
    display_world(first_world)

    next_world = compute_next_generation(first_world)
    print()
    display_world(next_world)

    for i in range(10):
        print()
        next_world = compute_next_generation(next_world)
        display_world(next_world)


if __name__ == "__main__":
    main()
