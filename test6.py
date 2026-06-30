#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'blacklist' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY amounts as parameter.
#


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    amounts = []

    for _ in range(k):
        amounts.append(list(map(int, input().rstrip().split())))

    result = blacklist(amounts)

    fptr.write(str(result) + '\n')

    fptr.close()
