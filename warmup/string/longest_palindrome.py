'''
Created on 14/11/2014

@author: c057384
'''

import sys

def print_matrix(m):
    
    print "\nMatrix:"
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            print m[i][j], 

        print

if __name__ == '__main__':
    s = sys.argv[1]
    
    if not s:
        sys.exit(0)
    
    longest = s[0]
    max_length = 1
    
    m = [[0 for x in xrange(len(s))] for x in xrange(len(s))] 
    
    for i in range(0, len(s)):        
        m[i][i] = 1
        
    print_matrix(m)
        
    for l in range(2, len(s) + 1):
        for i in range(0, len(s) - l + 1):
            j = i + l - 1
            
            if s[i] == s[j]:
                m[i][j] = m[i+1][j-1]
                
                if m[i][j] and l > max_length:
                    longest = s[i:j+1]
                    max_length = l                    
            else:
                m[i][j] = 0
            
    print_matrix(m)
    
    print "Longest:", longest
    print "Length", max_length