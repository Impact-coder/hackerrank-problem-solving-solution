#!/bin/python3

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
    count=0
    i=0
    while(i<len(c)-1):
        if(i+2==len(c)):
            count+=1
            break
        elif(i+1==len(c)):
            count+=1
            break
        
        if(c[i+2]==0):
            count+=1
            i+=2
        elif(c[i+1]==0):
            count+=1
            i+=1
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
