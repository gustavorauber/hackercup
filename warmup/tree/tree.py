'''
Created on 17/11/2014

@author: c057384
'''


class Node:
    left = None
    right = None
    value = None
    
    def __init__(self, value):
        self.value = value
            
    
def add_node(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            add_node(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            add_node(root.right, value)
            

def print_tree(root):
    queue = [root]
    
    while len(queue) > 0:
        new_queue = []
        
        for n in queue:
            print n.value, "\t",
            
            if n.left:
                new_queue.append(n.left)
            if n.right:
                new_queue.append(n.right)
        print
        queue = new_queue
        
    
    
        
