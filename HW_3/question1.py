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


def get_final_queue_order(input_file):
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
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        return list(queue)


def test_time_complexity():
    setup_code = "from question1 import get_final_queue_order"
    test_code = "get_final_queue_order('hw3_q1.txt')"
    time_taken = timeit.timeit(test_code, setup=setup_code, number=1000)  # Adjust the number of iterations as needed
    print(f"Time taken: {time_taken} seconds")


if __name__ == '__main__':
    print(get_final_queue_order('hw3_q1.txt'))
    test_time_complexity()

# note: or go through list and append all the joins, append all the jumps and concatenate the lists

# [B] What is the time and space complexity of your solution? If you are making
# any assumptions, list them.

# TIME AND SPACE COMPLEXITY:
# Time Complexity:
# The time complexity of this solution is O(N), where N is the number of lines in the input file.
# This is because the algorithm processes each line once, and the operations performed within
# each iteration (such as appending or appending to the left of the deque) are constant time.
#
# Space Complexity:
# The space complexity is also O(N), where N is the number of lines in the input file.
# The main contributor to space complexity is the deque, which stores the names of people
# in the queue. In the worst case, the deque could grow to accommodate all the names from
# the input file. The list conversion at the end doesn't significantly affect the overall
# space complexity, as it creates a new list with the same elements.
#
# In summary, the provided solution has a linear time complexity O(N) and a linear space
# complexity O(N), where N is the number of lines in the input file.


# ASSUMPTIONS:
# Input File Format: I am assuming the file follows the stated format of the question,
# i.e. 'The first word on each line will either be “JUMP” or “JOIN” and the second word the
# name of the person', and that each word is separated by a space (' '). I am also assuming
# that the file only contains the commands 'JUMP' or 'JOIN', otherwise it will raise an
# error.
#
# Command Handling Assumption: The code assumes that the only valid commands are "JUMP" and "JOIN,"
# and it correctly processes these commands to update the queue.
#
# File Existence Assumption: The code assumes that the input file (hw3_q1.txt) exists in the same
# directory as the script.
#
# Valid Input Data Assumption: The code assumes that the input data adheres to the described rules,
# and it does not perform extensive error checking for invalid or malformed input.
#
# Assuming that the file contains no blank lines
