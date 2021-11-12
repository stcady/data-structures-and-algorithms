from collections import deque

class Tree(object):

    # Node class representing elements of tree
    class Node:

        # Node class constructor for creating a new node
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.left_child = l
            self.right_child = r

    # Tree class constructor for creating a new list
    def __init__(self):
        self.root = None

    # level_order_binary_tree creates a binary tree from the values given in an array
    # complete binary tree is more efficient than skewed trees
    def level_order_binary_tree(self, arr, start):
        return self.level_order_binary_tree_util(arr, start)
    
    # level_order_binary_tree_util creates a binary tree recursive utility
    def level_order_binary_tree_util(self, arr, start):
        size = len(arr)
        curr = self.Node(arr[start])
        left = 2 * start + 1
        right = 2 * start + 2
        if left < size:
            curr.left_child = self.level_order_binary_tree_util(arr, left)
        if right < size:
            curr.right_child = self.level_order_binary_tree_util(arr, right)
        return curr
    
    # print_preorder prints the nodes in a tree via pre-order traversal
    # in pre-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print before recurse
    def print_preorder(self):
        self.print_preorder_util(self.root)
        
    # print_preorder_util prints the nodes in tree via recursive preorder
    def print_preorder_util(self, node):
        if node != None:
            print(node.value, end=' ')
            self.print_preorder_util(node.left_child)
            self.print_preorder_util(node.right_child)
            
    # nth_preorder prints the node at the nth index in a tree via pre-order traversal
    # in pre-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print before recurse
    def nth_preorder(self, index):
        count = 0
        self.nth_preorder_util(self.root, index, count)
        
    # print_preorder_util prints the node at the nth index in tree via recursive pre-order
    def nth_preorder_util(self, node, index, count):
        if node != None:
            count += 1
            if count == index:
                print(node.value, end=' ')
            self.nth_preorder_util(node.left_child, index, count)
            self.nth_preorder_util(node.right_child, index, count)
            
    # print_postorder prints the nodes in a tree via post-order traversal
    # in post-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print after recurse
    def print_postorder(self):
        self.print_postorder_util(self.root)
        
    # print_postorder_util prints the nodes in tree via recursive post-order
    def print_postorder_util(self, node):
        if node != None:
            self.print_postorder_util(node.left_child)
            self.print_postorder_util(node.right_child)
            print(node.value, end=' ')
            
    # nth_postorder prints the node at the nth index in a tree via post-order traversal
    # in post-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print before recurse
    def nth_postorder(self, index):
        count = 0
        self.nth_preorder_util(self.root, index, count)
        
    # print_postorder_util prints the node at the nth index in tree via recursive post-order
    def nth_postorder_util(self, node, index, count):
        if node != None:
            self.nth_preorder_util(node.left_child, index, count)
            self.nth_preorder_util(node.right_child, index, count)
            count += 1
            if count == index:
                print(node.value, end=' ')
            
    # print_inorder prints the nodes in a tree via in-order traversal
    # in in-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print inbetween recurse
    def print_inorder(self):
        self.print_inorder_util(self.root)
        
    # print_inorder_util prints the nodes in tree via recursive in-order
    def print_inorder_util(self, node):
        if node != None:
            self.print_inorder_util(node.left_child)
            print(node.value, end=' ')
            self.print_inorder_util(node.right_child)
            
    # nth_inorder prints the node at the nth index in a tree via in-order traversal
    # in in-order traversal, parent is traversed first, then left child subtree,
    # then right child subtree
    # print before recurse
    def nth_postorder(self, index):
        count = 0
        self.nth_preorder_util(self.root, index, count)
        
    # print_postorder_util prints the node at the nth index in tree via recursive in-order
    def nth_postorder_util(self, node, index, count):
        if node != None:
            self.nth_preorder_util(node.left_child, index, count)
            count += 1
            if count == index:
                print(node.value, end=' ')
            self.nth_preorder_util(node.right_child, index, count)
            
    # print_breadth_first prints the nodes in a tree via breath first traversal
    # all nodes at depth k are printed before nodes at depth k+1
    def print_breadth_first(self):
        que = deque([])
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            print(temp.value, end=' ')
            if temp.left_child != None:
                que.append(temp.left_child)
            if temp.right_child != None:
                que.append(temp.right_child)
                
    # print_depth_first prints the nodes in a tree via depth first traversal
    def print_depth_first(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        while len(stk) != 0:
            temp = stk.pop()
            print(temp.value, end=' ')
            if temp.right_child != None:
                stk.append(temp.right_child)
            if temp.left_child != None:
                stk.append(temp.left_child)
                
    # print_level_order prints the nodes in a tree via level order traversal
    def print_level_order(self):
        self.print_breadth_first()
        
    # print_spiral_tree prints the nodes in a tree in spiral order via breadth first traversal
    def print_spiral_tree(self):
        stk1 = []
        stk2 = []
        output = []
        temp = None
        if self.root != None:
            stk1.append(self.root)
        while len(stk1) != 0 or len(stk2) != 0:
            while len(stk1) != 0:
                temp = stk1.pop()
                output.append(temp.value)
                if temp.right_child != None:
                    stk2.append(temp.right_child)
                if temp.left_child != None:
                    stk2.append(temp.left_child)
            while len(stk2) != 0:
                temp = stk2.pop()
                output.append(temp.value)
                if temp.left_child != None:
                    stk1.append(temp.left_child)
                if temp.right_child != None:
                    stk1.append(temp.right_child)
        print(output)
        
    # print_all_paths prints all the paths from the roots to the leaf of a binary tree
    def print_all_paths(self):
        stk = []
        self.print_all_paths_util(self.root, stk)
        
    # print_all_paths_util prints all tree paths via recursion
    def print_all_paths_util(self, curr, stk):
        if curr == None:
            return
        stk.append(curr.value)
        if curr.left_child == None and curr.right_child == None:
            print(stk)
            stk.pop()
            return
        self.print_all_paths_util(curr.right_child, stk)
        self.print_all_paths_util(curr.left_child, stk)
            
    # num_nodes finds the total number of nodes in a binary tree
    def num_nodes(self):
        return self.num_nodes_util(self.root)

     
    # num_nodes_utils counts number of nodes via recursion
    def num_nodes_util(self, curr):
         if curr == None:
             return 0
         else:
             return (1 + self.num_nodes_util(curr.right_child) + self.num_nodes_util(curr.left_child))