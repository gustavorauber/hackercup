'''
Created on 17/11/2014

@author: c057384
'''

from tree import *

def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if root is None:
        return 0
    return 1 + min(min_depth(root.left), min_depth(root.right))

def is_balanced(root):
    """
    4.1 - Check if a tree is balanced
    """
    x_max = max_depth(root)
    x_min = min_depth(root)
    
    print "Max Depth", x_max
    print "Min Depth", x_min
    
    return (x_max - x_min) <= 1

if __name__ == '__main__':
    root = Node("J")    
    
    # Left Branch, max height = 5, min height = 3
    add_node(root, "G")
    add_node(root, "H")
    add_node(root, "E")
    add_node(root, "C")
    add_node(root, "A")
    
    # Right Branch, max height = 2, min height = 3
    add_node(root, "L")
    add_node(root, "K")
    add_node(root, "M")
    
    print_tree(root)
    
    print is_balanced(root)
