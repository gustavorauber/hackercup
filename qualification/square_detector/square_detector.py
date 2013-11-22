#!/usr/bin/env python

def is_square(square, n):
    count_black_cells = 0
    black_lines = set()
    black_indexes = set()
    num_black_indexes = 0
    black_removed = False
    
    for k in range(0, n):
        line_indexes = set()
        line = square[k]        
        
        if len(black_indexes) == 0:
            add_black_indexes = True
        else:
            add_black_indexes = False
        
        for j, value in enumerate(line):
            if value == "#":
                count_black_cells += 1
                black_lines.add(k)
                line_indexes.add(j)
                
                if add_black_indexes:
                    black_indexes.add(j)
                elif j not in black_indexes:
                     return False
            elif not add_black_indexes and j in black_indexes:
                black_indexes.remove(j)            
                
        if add_black_indexes and len(black_indexes) > 0:
            num_black_indexes = len(black_indexes)
            black_removed = True       
            
        if len(line_indexes) > 0 and \
        len(black_indexes.intersection(line_indexes)) != num_black_indexes:
            return False         

    if count_black_cells == 1:
        return True
    elif len(black_lines) != num_black_indexes:
        return False    
    
    return True

if __name__ == "__main__":
    t = int(raw_input().strip())
    
    for i in range(1, t + 1):
        n = int(raw_input().strip())
        square = []
        
        for line in range(0, n):
            square.append(raw_input().strip())        
        
        answer = "YES" if is_square(square, n) else "NO"
        print "Case #{0}: {1}".format(i, answer)
        