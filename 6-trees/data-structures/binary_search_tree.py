from binary_tree import Tree
import sys

class BinarySearchTree(Tree):

    # create creates a binary search tree from a sorted array
    def create(self, arr):
        self.root = self.create_util(arr, 0, len(arr) - 1)
    
    # create_util creates a binary search tree from a sorted array via recursion
    def create_util(self, arr, start, end):
        if start > end:
            return None
        mid = ((start + end) // 2)
        curr = self.Node(arr[mid])
        curr.left_child = self.create_util(arr, start, mid - 1)
        curr.right_child = self.create_util(arr, mid + 1, end)
        return curr
    
    # insert_node inserts a node into a binary search tree
    def insert_node(self, node, value):
        return self.insert_node_util(node, value)
    
    # insert_node_util inserts a node into a binary search tree via recursion
    def insert_node_util(self, node, value):
        if node == None:
            node = self.Node(value)
        else:
            if node.value > value:
                node.right_child = self.insert_node_util(node.left_child, value)
            else:
                node.left_child = self.insert_node_util(node.right_child, value)
        return node
    
    # find_node traverses the binary search tree to find the node with the value given
    def find_node(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.left_child
            else:
                curr = curr.right_child
        return False
    
    # find_min traverses the binary search tree to find the node with the minimum value
    def find_min(self):
        node = self.root
        if node == None:
            raise RuntimeError("TreeEmptyException")
        while node.left_child != None:
            node = node.left_child
        return node
    
    # find_max traverses the binary search tree to find the node with the maximum value
    def find_max(self):
        node = self.root
        if node == None:
            raise RuntimeError("TreeEmptyException")
        while node.right_child != None:
            node = node.right_child
        return node
    
    # is_bst determines if the provided tree is a binary search tree
    def is_bst(self):
        count = [0]
        return self.is_bst_util(self.root, count)
    
    # is_bst_util does an in-order traversal of nodes and checks if it is strictly increasing
    def is_bst_util(self, curr, count):
        # in-order traversal
        ret = bool()
        if curr != None:
            ret = self.is_bst_util(curr.left_child, count)
            if not ret:
                return False
            if count[0] > curr.value:
                return False
            count[0] = curr.value
            ret = self.is_bst_util(curr.right_child, count)
            if not ret:
                return False
        return True
    
    # delete_node deletes a node from the binary search tree
    def delete_node(self, value):
        self.root = self.delete_node_util(self.root, value)
        
    # delete_node_util deletes a node from a binary search tree via recursion
    def delete_node_util(self, node, value):
        temp = None
        if node != None:
            if node.value == value:
                # 0 children case
                if node.left_child == None and node.right_child == None:
                    return None
                else:
                    # 1 child case on right
                    if node.left_child == None:
                        temp = node.right_child
                        return temp
                    # 1 child case on left
                    if node.right_child == None:
                        temp = node.left_child
                        return temp
                    # 2 children case
                    maxnode = self.find_max_util(node.left_child)
                    node.value = maxnode.value
                    node.left_child = self.delete_node_util(node.left_child, maxnode.value)
            else:
                if node.value > value:
                    node.left_child = self.delete_node_util(node.left_child, value)
                else:
                    node.right_child = self.delete_node_util(node.right_child, value)
        return node
    
    # lca finds the least common ancestor
    def lca(self, first, second):
        ans = self.lca_util(self.root, first, second)
        if ans != None:
            return ans.value
        return sys.maxsize

    # lca_util finds the least common ancestor via recursion
    def lca_util(self, curr, first, second):
        if curr == None:
            return None
        if curr.value == first or curr.value == second:
            return curr
        left = self.lca_util(curr.left, first, second)
        right = self.lca_util(curr.right, first, second)
        if left != None and right != None:
            return curr
        elif left != None:
            return left
        else:
            return right
        
    # trim_outside_range removes nodes outside the specified range
    def trim_outside_range(self, minval, maxval):
        self.trim_outside_range_util(self.root, minval, maxval)

    # trim_outside_range_util removes the nodes outside the specified range via recursion
    def trim_outside_range_util(self, curr, minval, maxval):
        if curr == None:
            return None
        curr.left = self.trim_outside_range_util(curr.left, minval, maxval)
        curr.right = self.trim_outside_range_util(curr.right, minval, maxval)
        if curr.value < minval:
            return curr.right
        if curr.value > maxval:
            return curr.left
        return curr
    
    # print_in_range prints the tree values in the specified range
    def print_in_range(self, minval, maxval):
        self.print_in_range_util(self.root, minval, maxval)
        print()

    # print_in_range_util prints the tree values in the specified range via recursion
    def print_in_range_util(self, root, minval, maxval):
        if root == None:
            return
        self.print_in_range_util(root.left, minval, maxval)
        if root.value >= minval and root.value <= maxval:
            print(root.value, end=' ')
        self.print_in_range_util(root.right, minval, maxval)
        
    # ceil_bst finds the ceiling value in a binary search tree
    def ceil_bst(self, val):
        curr = self.root
        ceil = -1 * (sys.maxunicode)
        while curr != None:
            if curr.value == val:
                ceil = curr.value
                break
            elif curr.value > val:
                ceil = curr.value
                curr = curr.left
            else:
                curr = curr.right
        return ceil
    
    # floor_bst finds the floor value in a binary search tree
    def floor_bst(self, val):
        curr = self.root
        floor = sys.maxsize
        while curr != None:
            if curr.value == val:
                floor = curr.value
                break
            elif curr.value > val:
                curr = curr.left
            else:
                floor = curr.value
                curr = curr.right
        return floor
    
    # is_bst_array checks if an array is a preorder traversal of a binary search tree
    def is_bst_array(preorder):
        size = len(preorder)
        stk = []
        root = -sys.maxsize
        i = 0
        while i < size :
            value = preorder[i]
            # If value of the right child is less than root.
            if (value < root):
                return False
            # First left child values will be popped
            # Last popped value will be the root.
            while (len(stk) > 0 and stk[len(stk) - 1] < value) :
                root = stk.pop()
            
            # add current value to the stack.
            stk.append(value)
            i += 1

        return True