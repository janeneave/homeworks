# [A] Write a program that takes in an input file and prints out a list with the final
# order of who’s in the queue.
# You are expected to use the provided input file hw3_q1.txt to develop and test your
# solution.
# The first word on each line will either be “JUMP” or “JOIN” and the second word the
# name of the person, the word “JUMP” means the person in question has gone to
# the front of the queue, if the word is “JOIN” it means they have joined the back of
# the queue.
# You are expected to identify and use a container from the collections module for
# your solution.

from collections import deque
import timeit
from typing import List


def get_final_queue_order(input_file):
    # Using a deque (Doubly ended queue) to "append" (& "appendleft") from both ends of the container.
    queue = deque()
    try:
        with open(input_file, 'r') as text_file:
            for line in text_file:
                line = line.strip()
                if not line:
                    continue
                command, name = line.split(' ')
                if command == 'JUMP':
                    queue.appendleft(name)
                elif command == 'JOIN':
                    queue.append(name)
    except FileNotFoundError:
        print(f'File not found: {input_file}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    else:
        return list(queue)


def test_time_complexity():
    setup_code = 'from question1 import get_final_queue_order'
    test_code = 'get_final_queue_order("hw3_q1.txt")'
    time_taken = timeit.timeit(test_code, setup=setup_code, number=1000)
    print(f'Time taken: {time_taken} seconds')


if __name__ == '__main__':
    print(get_final_queue_order('hw3_q1.txt'))
    test_time_complexity()

# note:or go through list and append all the joins, append all the jumps and concatenate the lists/work frm middle out

# [B] What is the time and space complexity of your solution? If you are making
# any assumptions, list them.

# TIME AND SPACE COMPLEXITY:
# Time Complexity:
# For this function the time complexity is primarily determined by the for loop that iterates
# through each line of the input_file.
# .strip() and .split() are constant time operations.
# It is the append() and appendleft() methods which contribute most to the time complexity.
# Using a deque() provides a O(1) time complexity for append() and appendleft(), as they both take constant time.
# (Unlike if they were used in a list which would provide O(N) complexity).
# Nevertheless, the loop iterates through each line in the input_file once, therefore the overall time complexity
# is O(N), whereby N is the number of lines in the file, and append operations are performed once within each iteration
# and are constant time.

# Space Complexity:
# This is determined by the additional memory used by my solution (excluding input space).
# The main contributor to space complexity is the deque, which is the primary data structure which
# stores the names of people in the queue. In the worst case, the deque could grow to accommodate all the names from
# the input file. It's space complixity is O(N), where N is the number of names in the queue.
# Other variables, such as line, command and name contribute space O(1).
# The list conversion at the end doesn't significantly affect the overall space complexity,
# as it creates a new list with the same elements of the deque. It has a space complexity of O(N) because the new
# list created is of size N.
# Thus, for my solution the overall space complexity is O(N), whereby N is the number of names in the queue.

# In summary, the provided solution has a linear time complexity O(N) and a linear space
# complexity O(N), where N is the number of lines in the input file.

# ASSUMPTIONS:
# I am assuming the input_file follows the stated format of the question,
# i.e. 'The first word on each line will either be “JUMP” or “JOIN” and the second word the
# name of the person', and that each word is separated by a space (' '). I am also assuming
# that the file only contains the commands 'JUMP' or 'JOIN', otherwise it will raise an
# error. Additionally, I am assuming that the file is not empty and contains text.
# Assuming that the file exists, and that the function will handle a FileNotFoundError.
# Assuming that function handles unexpected errors during file processing with the Exception.
