from collections import deque
from sys import tracebacklimit

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
         
    # sum_all_nodes finds the sum of values of all nodes in a binary tree
    def sum_all_nodes(self):
        return self.sum_all_nodes_util(self.root)
    
    
    # sum_all_nodes_util sums the nodes via recursion
    def sum_all_nodes_util(self, curr):
        if curr == None:
            return 0
        right_sum = self.sum_all_nodes_util(curr.right_child)
        left_sum = self.sum_all_nodes_util(curr.left_child)
        finalsum = right_sum + left_sum + curr.value
        return finalsum
    
    # num_leaf_nodes finds the number of leaf nodes in a binary tree
    def num_leaf_nodes(self):
        return self.num_leaf_nodes_util(self.root)
    
    # num_leaf_nodes_util finds the number of leaf nodes recursivley
    def num_leaf_nodes_util(self, curr):
        if curr == None:
            return 0
        if curr.left_child == None and curr.right_child == None:
            return 1
        else:
            return (self.num_leaf_nodes_util(curr.right_child) + self.num_leaf_nodes_util(curr.left_child))
        
    # num_full_nodes finds the number of full nodes in a binary tree
    def num_full_nodes(self):
        return self.num_full_nodes_util(self.root)
    
    # num_full_nodes_util finds the number of full nodes via recursion
    def num_full_nodes_util(self, curr):
        if curr == None:
            return 0
        count = self.num_leaf_nodes_util(curr.right_child) + self.num_leaf_nodes_util(curr.left_child)
        if curr.left_child != None and curr.right_child != None:
            count += 1
        return count
    
    # search_tree searches for a particular value in the binary tree
    def search_tree(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True
        left = self.search_tree(root.left_child, value)
        if left:
            return True
        right = self.search_tree(root.right_child, value)
        if right:
            return True
        return False
    
    # find_max finds the maximum value in a binary tree
    def find_max(self):
        ans = self.find_max_util(self.root)
        return ans
    
    # find_max_util finds the maximum value via recursion
    def find_max_util(self, curr):
        if curr == None:
            return None
        maxval = curr.value
        left = self.find_max_util(curr.left_child)
        right = self.find_max_util(curr.right_child)
        if left > maxval:
            maxval = left
        if right > maxval:
            maxval = right
        return maxval
    
    # tree_depth finds the depth of a binary tree
    def tree_depth(self):
        return self.tree_depth_util(self.root)
    
    # tree_depth_util finds the depth via recursion
    def tree_depth_util(self, root):
        if root == None:
            return 0
        else:
            left_depth = self.tree_depth_util(root.left_child)
            right_depth = self.tree_depth_util(root.right_child)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
            
    # max_length_path finds the maximum length path in a binary tree
    def max_length_path(self):
        return self.max_length_path(self, self.root)
    
    # max_length_path_util finds the maximum length path via recursion
    def max_length_path_util(self, curr):
        if curr == None:
            return 0
        left_path = self.max_length_path_util(curr.left_child)
        right_path = self.max_length_path_util(curr.right_child)
        maxpath = left_path + right_path + 1
        left_max = self.max_length_path_util(curr.left_child)
        right_max = self.max_length_path_util(curr.right_child)
        if left_max > maxpath:
            maxpath = left_max
        if right_max > maxpath:
            maxpath = right_max
        return maxpath
    
    # is_equal determines if two trees are equal
    def is_equal(self, T2):
        return self.is_equal_util(self.root, T2.root)

    # is_equal_util determines if two trees are equal via recursion
    def is_equal_util(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return (self.is_equal_util(node1.left_child, node2.left_child) and self.is_equal_util(node1.right_child, node2.right_child) and (node1.value == node2.value))
    
    # copy_tree copies the values to another binary tree
    def copy_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_tree_util(self.root)
        return tree2

    # copy_tree_util copies the values to another binary tree via recursion
    def copy_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.left = self.copy_tree_util(curr.left_child)
            temp.right = self.copy_tree_util(curr.right_child)
            return temp
        else:
            return None
    
    # copy_mirror_tree copies the values to another binary tree as a mirror image
    def copy_mirror_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_mirror_tree_util(self.root)
        return tree2

    # copy_mirror_tree_util copies the values to another binary tree as a mirror image via recursion
    def copy_mirror_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.right = self.copy_mirror_tree_util(curr.left_child)
            temp.left = self.copy_mirror_tree_util(curr.right_child)
            return temp
        else:
            return None
        
    # free_tree frees all nodes in the tree
    def free(self):
        self.root = None
        
    # find_count 
    def find_count(self):
        return self.find_count_util(self.root)
    
    # find_count_util
    def find_count_util(self, curr):
        if curr == None:
            return 0
        return (1 + self.find_count_util(curr.left) + self.find_count_util(curr.right))
        
    # is_complete_tree determines if the tree is complete
    def is_complete_tree(self):
        count = self.find_count()
        return self.is_complete_tree_util(self.root, 0, count)
        
    # is_complete_tree_util determines if the tree is complete via recursion
    def is_complete_tree_util(self, curr, index, count):
        if curr == None:
            return True
        if index > count:
            return False 
        return self.is_complete_tree_util(curr.left, index*2+1, count) and self.is_complete_tree_util(curr.right, index*2+2, count)

    # is_heap determines if the tree is a heap
    def is_heap(self):
        return self.is_complete_tree() and self.is_heap_util(self.root, None)
    
    # is_heap_util determines if the tree is a heap via recursion
    def is_heap_util(self, curr, parent_value):
        if curr == None:
            return True
        if curr.value < parent_value:
            return False
        return (self.is_heap_util(curr.left, curr.value) and self.is_heap_util(curr.right, curr.value))
    
    # iterative_preorder performs preorder traversal without recursion
    def iterative_preorder(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        while len(stk) != 0:
            curr = stk.pop()
            print(curr.value, end=' ')
            if curr.right_child != None:
                stk.append(curr.right_child)
            if curr.left_child != None:
                stk.append(curr.left_child)
                
    # iterative_postorder performs postorder traversal without recursion
    def iterative_postorder(self):
        stk = []
        visited = []
        if self.root != None:
            stk.append(self.root)
            visited.append(0)
        while len(stk) != 0:
            curr = stk.pop()
            vtd = visited.pop()
            if vtd == 1:
                print(curr.value, end=' ')
            else:
                stk.append(curr)
                visited.append(1)
                if curr.right_child != None:
                    stk.append(curr.right_child)
                    visited.append(0)
                if curr.left_child != None:
                    stk.append(curr.left_child)
                    visited.append(0)
        
    # iterative_inorder performs inorder traversal without recursion
    def iterative_inorder(self):
        stk = []
        visited = []
        if self.root != None:
            stk.append(self.root)
            visited.append(0)
        while len(stk) != 0:
            curr = stk.pop()
            vtd = visited.pop()
            if vtd == 1:
                print(curr.value, end=' ')
            else:
                if curr.right != None:
                    stk.append(curr.right)
                    visited.append(0)
                stk.append(curr)
                visited.append(1)
                if curr.left != None:
                    stk.append(curr.left)
                    visited.append(0)
                    
    # tree2list creates a doubly linked list from a binary tree via inorder traversal
    def tree2list(self, curr):
        if curr == None:
            return None
        if curr.left_child == None and curr.right_child == None:
            curr.left_child == curr
            curr.right_child == curr
            return curr
        if curr.left_child != None:
            head = self.tree2list(curr.left_child)
            tail = head.left_child
            curr.left_child = tail
            tail.right_child = curr
        else:
            head = curr
        if curr.right_child != None:
            temp_head = self.tree2list(curr.right_child)
            tail = temp_head.left_child
            curr.right_child = temp_head
            temp_head.left_child = curr
        else:
            tail = curr
        head.left_child = tail
        tail.right_child = head
        return head