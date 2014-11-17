'''
Created on 17/11/2014

@author: c057384
'''

import sys

if __name__ == '__main__':
    """
    5.1 - Bit Manipulation
    """
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    i = int(sys.argv[3])
    j = int(sys.argv[4])    
     
    max_mask = 0xFFFFFFFF # 32-bit mask    
  
    # Grab (i,j) substring from M    
    # Clears (i,j) part in N
    left = max_mask - ((1 << j) - 1)
    right = ((1 << i) - 1)
    mask = left | right
    
    result = (n & mask) | (m << i)
    
    print "M = {0:b}".format(m)
    print "N = {0:b}".format(n)
    print "X = {0:b}".format(result)
