import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import ListNode

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
       
        if(value < self.value):
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif(value >= self.value):
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    
    def contains(self, target):
        #Start by comparing the target value
        if target < self.value:#If less, check if node is empty, then reached base case and target doesn't exist in the tree
            if self.left is None:
                return False
            return self.left.contains(target)#Otherwise recursion from left node and try finding it
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:#if target value isn't less or greater, then it found the node
            return True

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):#Run the function the, start recursion on left and right, it will be stop once functions runs on all nodes
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
