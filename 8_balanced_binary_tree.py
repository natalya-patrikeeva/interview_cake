# Write a function to see if a binary tree is "superbalanced".
# A tree is "superbalanced" if the difference between the depths of any two
# leaf nodes is no greater than one.

# Depth-first search to reach leaves faster
# Keep track of every leaf depth
# If more than 2 depths or 2 depths but their difference > 1, return False

# O(n) time and O(n) space
def is_superbalanced(root) :

    if not root:
        return True

    nodes = []

    # Save node visited and its depth starting at a root node with depth 0
    # Use a stack to store tuples 
    nodes.append( (root, 0) )

    # Keep track of depths
    depths = []

    # traverse a tree
    while len(nodes) :
        print "len(nodes)", len(nodes)
        node, depth = nodes.pop()
        print "node, depth", node.value, depth

        # Leaf node if it doesn't have descendants
        if (not node.left) and (not node.right):

            if depth not in depths:
                depths.append(depth)

                # Check to see if depths break superbalanced definition
                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1 ):
                    return False

        # Not a leaf. Keep traversing down the tree
        else:
            if node.left :
                nodes.append( (node.left, depth + 1))
            if node.right :
                nodes.append( (node.right, depth + 1))


    return True

# Binary Tree Node class
class BinaryTreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# Testing to see if the tree is superbalanced
tree_root = BinaryTreeNode(4)
tree_root.insert_right(6)
tree_root.insert_left(2)
print(is_superbalanced(tree_root))
