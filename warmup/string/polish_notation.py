'''
Created on 12/11/2014

Deals with polish notation expressions

e.g: 21+3* (result = 9)

@author: c057384
'''

import sys

if __name__ == '__main__':
    expression = sys.argv[1]    
    stack = []
    
    result = 0
    
    for s in expression:
        if s in "+-*/":
            a = stack.pop()
            b = stack.pop()
            
            if s == "+":
                stack.append(a + b)
            elif s == "-":
                stack.append(b - a)
            elif s == "*":
                stack.append(a * b)
            elif s == "/":
                stack.append(b / float(a))
                
        else:
            stack.append(int(s))

    result = stack.pop()        
    print result