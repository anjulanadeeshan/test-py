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

def blacklist(amounts):
    # Write your code here
    if not amounts or not amounts[0] :
        return 0;

    k = len(amounts)
    n = len(amounts[0])



    return res;

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    amounts = []

    for _ in range(k):
        amounts.append(list(map(int, input().rstrip().split())))
import sys

# Increase recursion depth just in case for deep DP states
sys.setrecursionlimit(2000)

def solve():
    # Read N (gangsters) and K (mercenaries)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    # Grid of charges: K lines, each containing N integers
    # cost[i][j] is the cost of mercenary i killing gangster j
    costs = []
    idx = 2
    for i in range(K):
        row = []
        for j in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        costs.append(row)
        
    # Memoization table to store computed subproblems
    memo = {}
    
    def get_min_cost(g_idx, mask):
        # Base case: All gangsters have been eliminated
        if g_idx == N:
            return 0
            
        state = (g_idx, mask)
        if state in memo:
            return memo[state]
        
        min_total = float('inf')
        
        # Try all possible consecutive groups starting from g_idx
        for next_g in range(g_idx + 1, N + 1):
            # Try assigning this segment to any available mercenary
            for m in range(K):
                if not (mask & (1 << m)):  # If mercenary m is free
                    # Calculate the cost for mercenary m to kill gangsters from g_idx to next_g - 1
                    current_cost = sum(costs[m][g_idx:next_g])
                    
                    # Recursively solve for the remaining gangsters with the updated mask
                    total = current_cost + get_min_cost(next_g, mask | (1 << m))
                    if total < min_total:
                        min_total = total
                        
        memo[state] = min_total
        return min_total

    # Start from gangster 0 with no mercenaries used (mask = 0)
    print(get_min_cost(0, 0))

if __name__ == '__main__':
    solve()
    result = blacklist(amounts)

    fptr.write(str(result) + '\n')

    fptr.close()
