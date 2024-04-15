# Ryan Lu, Anthony Thornton
# Dr. Sampson Akwafuo
# CPSC 335-04
# 2024, April 10

# Emails : rlu132@csu.fullerton.edu anthonythornton140@csu.fullerton.edu

import time
import csv
from numpy import random
from time import sleep

def verify(G, moves, ROW, COLUMN):
    row = col = 0
    # Make each move in candidate solution
    for i in range(len(moves)):
        # Check if current position is blocked
        if G[row][col] == 'X':
            return False
        # Decide to move right or down
        if moves[i] == 1:
            col += 1
        if moves[i] == 0:
            row += 1
        # Check for out of bounds
        if row >= ROW or col >= COLUMN:
            return False
    # Check if moves lead to correct cell and last cell is open
    return True if row == ROW - 1 and col == COLUMN - 1 and G[row][col] == '.' else False

def soccer_exhaustive(G, ROW, COLUMN):
    len = ROW + COLUMN - 2
    counter = 0
    for bits in range(2**(len)):
        candidate = []
        # Generate candidates
        for k in range(len):
            bit = (bits >> k) & 1 
            if bit == 1:
                candidate.append(1)
            else: 
                candidate.append(0)
        # verify current candidate (candidates without len number of moves will not reach the end)
        if verify(G, candidate, ROW, COLUMN):
            counter+= 1
    return counter

def soccer_dynamic(F,ROW, COLUMN):
    # Base case
    if F[0][0] == 'X':
        return 0
    A = [[0 for i in range(COLUMN)] for j in range(ROW)] #Intialize matrix A with zeroes
    A[0][0] = 1
    # Loop through matrix
    for i in range(ROW):
        for j in range(COLUMN):
            # If current cell is blocked, set possible paths to position to 0 in A
            if F[i][j] == 'X':
                A[i][j] = 0
                continue
            above = left = 0
            # If above or left cell is unblocked add possible paths to current cell in A
            if i > 0 and F[i - 1][j] == '.':
                above = A[i - 1][j]    
            if j > 0 and F[i][j - 1] == '.':
                left = A[i][j - 1]
            A[i][j] += above + left
    # Return number of possible paths to last cell in A
    return A[ROW - 1][COLUMN - 1] 

def print_field(field):
    # Print the field verticaly in a more readable fashion
    for i in range(len(field)):
        print(field[i])

def generate_field():
    # Generate a random field of .'s and X's of with width ranging from 9-14 and height ranging from 8-13
    # Slightly manipulate the ratio of .'s to X's to be around 1:4 for fields that are more likely to be traversed
    rows, cols = random.randint(8,13),random.randint(9,14)
    temp = random.randint(low = 0, high = 5, size = (rows, cols))
    # New field to change ints to '.' and 'X'
    field = [[0 for i in range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if temp[row][col] > 0:
                field[row][col] = '.'
            else:
                field[row][col] = 'X'
    return field
    
def test(field):
    # Find dimensions of randomly generated field
    field_cols, field_rows = len(field[0]), len(field)
    field_size = field_rows*field_cols
    print_field(field)

    # Measure time for exhaustive algorithm
    start_time = time.time()
    result = soccer_exhaustive(field, field_rows, field_cols)
    exhaustive_time = (time.time() - start_time)
    print("Exhaustive: %s seconds" % exhaustive_time)
    print("Exhaustive result: %s" % result)

    # Measure time for dynamic algorithm
    start_time = time.time()
    result = soccer_dynamic(field, field_rows, field_cols)
    dynamic_time = (time.time() - start_time)
    print("Dynamic: %s seconds" % dynamic_time)
    print("Dynamic result: %s\n" % result)

    return [field_size, exhaustive_time, dynamic_time]


print('Starting')
# For reproducable results
random.seed(0)

example_field = [['.','.','.','.','.','.','X','.','X'], ['X', '.','.','.','.','.','.','.','.'], ['.','.','.','X','.','.','.','X', '.'], ['.','.','X','.','.','.','.','X','.'], ['.','X','.','.','.','.','X','.','.'], ['.','.','.','.','X','.','.','.','.'], ['.','.','X','.','.','.','.','.','X'], ['.','.','.','.','.','.','.','.','.']]

# Open csv file to write results of tests
with open('oap_comparison.csv', 'w', newline='') as csv_file:
    # Create a writer and write header for columns
    writer = csv.writer(csv_file)
    writer.writerow(['Instance Size', 'Exhaustive', 'Dynamic'])
    # Run the test 20 times
    for i in range(20):
        print("Running test #%s" % (i+1))
        # Randomly generated field, details in function definition
        field = generate_field()
        result = test(field)
        # Write instance size, time for exhaustive algorithm, and time for dynamic algorithm for that specific instance to csv file
        writer.writerow(result)
csv_file.close()

print("Testing example field with solution of 102:")
test(example_field)

print('Finished, test session results can be found in oap_comparison.csv')