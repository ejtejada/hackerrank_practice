#!/usr/bin/python3
#Based on warm up by HackerRank user Shafaet
#Author Edgar Tejada
import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    #This is a variation of a shortest path problem, where likely the greedy algorithm will NOT always work. 
    #Possible approach is bad, trying every possible path :/
    
    jumps_to_completion = 0; #Initialize output
    #First iteration, the greedy approach
    #print(type(c[0])); #[DELETE_ME] Just a sanity type check 
    jumps_to_completion = jumpingOnGreed(c);
    
    return (jumps_to_completion);

#Not an optimal solution, this will fail when greedy algo will fail!
def jumpingOnGreed(c):
	jumps_to_completion = 0; #Hacky offset, not clean 
	last_step = 0;
	bool_death = False;
	#Current approach, jump greedily unless this causes death, then backtrace to a safer jump
	for i in range(0,len(c)-2):
		if(bool_death):
			print(i);
			print('We backtraced');
			#Next legal moves cause death, go back
			i = i - 1 -  last_step;
			jumps_to_completion = jumps_to_completion - 1;
		elif ((c[i] == 0) and (c[i+2] == 0) and (i+2) < len(c) and not bool_death):
			print(i);
			jumps_to_completion = jumps_to_completion + 1;
			i = i + 1; #Skip a step greedily
			last_step = 2;
			bool_death = False;
			
		elif((c[i] == 0) and (c[i+1] == 0) and (i+1) < len(c) and not bool_death):
			print(i);
			jumps_to_completion = jumps_to_completion + 1;
			last_step = 1;
			bool_death = False;
		elif((c[i] == 1)): #We landed on a thunderhead and died, backtrace
			print(i);
			print('We died');
			bool_death = True;
	
	return (jumps_to_completion);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
