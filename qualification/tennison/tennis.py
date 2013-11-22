#!/usr/bin/env python

if __name__ == "__main__":
    t = int(raw_input().strip())
   
    for i in range(1, t + 1):
        params = raw_input().strip().split()
        
        k = int(params[0])
        p = 1.0
        p_s = float(params[1])
        p_r = float(params[2])
        p_i = float(params[3])
        p_u = float(params[4])
        p_w = float(params[5])
        p_d = float(params[6])
        p_l = float(params[7])
        
        for current_set in range(0, k):
            p_set = p_s * p_i            
            p_set += p_r * (1 - p_i)
            p_set = min(max(p_set, 0), 1)
                    
            
            p_i += p_set * p_w * p_u
            p_i = min(max(p_i, 0), 1)
        
            p_i -= (1 - p_set) * p_l * p_d
            p_i = min(max(p_i, 0), 1)                            
            
#             print p_set, p_i
            
            p *= p_set     
        
        print "Case #{0}: {1:6f}".format(i, p)