#!/usr/bin/python3
#Based on warm up by HackerRank
#Author Edgar Tejada

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
	
    # Write your code here
    #Firstly, this state assumes inputs are correct, that steps is an integer, and path is a String path
    #[TODO] Handle excepions here for illegal inputs or sanitize bad inputs.
    valleys_travelled = 0; #Initialize output
	current_elevation = 0;
	up_token = 'U';
	down_token = 'D';
	in_valley_bool = False; #Base case of sealevel
    for i in range(0, steps):
		if(path[i].lower() == up_token.lower()):
			current_elevation = current_elevation + 1;
		elif(path[i].lower() == down_token.lower()):
			current_elevation = current_elevation - 1;
		else:
			#Somethign went wrong, [TODO] throw exceptions
			print('Illegal inputs for transit detected');
			
		if(current_elevation < 0 and not in_valley_bool):
			#Only up the counter when we first enter a valley
			valleys_travelled = valleys_travelled + 1;
			in_valley_bool = True;
		elif(current_elevation >=0 and in_valley_bool):
			#We climbed out of the valley
			in_valley_bool = False;
		
    return(valleys_travelled)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
