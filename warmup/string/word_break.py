'''
Created on 14/11/2014

@author: c057384
'''

import sys

def read_dict(f_name):
    d = set()
    
    with open(f_name, "r") as f:
        for line in f:
            d.add(line.strip()) 
    
    return d

def check_phrase(phrase, words):
    #WRONG
    wb = [False for i in xrange(len(phrase) + 2)]    
    
    for l in range(1, len(phrase) + 1):   
        print l, phrase[0:l]     
        if not wb[l] and phrase[0:l] in words:
            wb[l] = True            
            
        if wb[l]:
            print "yo"
            if l + 1 == len(phrase):
                print "GOOD", l + 1
                return True
            
            for j in range(l + 2, len(phrase) + 2):                
                print j, l, j - l + 3, phrase[l:j-l + 3], phrase[l]
                if not wb[j] and phrase[l:j-l + 3] in words:
                    wb[j] = True
                    
                if j + 1 == len(phrase) and wb[j]:
                    print "GOOD", j + 1
                    return True
    return False

if __name__ == '__main__':
    dict_file = sys.argv[1]
    words = read_dict(dict_file)    
    phrase = sys.argv[2]
    
    print words
    print check_phrase(phrase, words)
    