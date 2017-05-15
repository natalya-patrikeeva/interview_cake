# Write a function to check that a binary tree is a valid binary search tree.

# Depth-first walk through the tree, testing each node for validity as we go.
# O(n) time and O(n) space complexity.
def is_bst(root) :

    # store node, its lower and upper bounds in a stack
    node_and_bounds_stack = [ (root, -float('inf'), float('inf')) ]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # check if not is invalid, return False
        if (node.value <= lower_bound) or (node.value >= upper_bound) :
            return False

        if node.left :
            node_and_bounds_stack.append( ( node.left, lower_bound, node.value ))

        if node.right :
            node_and_bounds_stack.append( ( node.right, node.value, upper_bound))

    return True

# Recursive solution
def is_bst_recursive(root, lower_bound = -float('inf'), upper_bound = float('inf')):

    if not root:
        return True

    if (root.value <= lower_bound) or (root.value >= upper_bound) :
        return False

    return is_bst_recursive(root.left, lower_bound, root.value) \
        and is_bst_recursive(root.right, root.value, upper_bound)


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# test
tree_root = BinaryTreeNode(5)
tree_root.insert_right(7)
tree_root.insert_left(3)

print(is_bst(tree_root))
