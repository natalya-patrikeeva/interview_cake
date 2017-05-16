# Write a function to find the 2nd largest element in a binary seach tree.

# Recursive solution
# O(h) time and O(h) space where h is the height of the tree
# O(lg(n)) for a balanced tree; O(n) if not balanced 
# find the rightmost node
def find_largest_recursive(root) :
    if root.right :
        return find_largest_recursive(root.right)
    return root.value


# find the second largest node
def find_second_largest_recursive(root) :

    # current node is the largest and it has a left subtree
    if root.left and not root.right :
        return find_largest_recursive( root.left )

    # current node is the parent of the largest node
    # largest node does not have a left subtree
    if root.right and not root.right.left and not root.right.right :
        return root.value

    # else, step right
    return find_second_largest_recursive(root.right)


# Iterative solution without recursion
# O(h) time and O(1) space

def find_largest(root) :
    current = root
    while current:
        if not current.right :
            return current.value

        current = current.right

def find_second_largest(root):
    if not root or (not root.left and not root.right) :
        raise Exception('Tree must have at least 2 nodes')

    current = root
    while current:
        # current node is the largest and it has a left subtree
        if current.left and not current.right :
            return find_largest( current.left )

        # current node is the parent of the largest node
        # largest node does not have a left subtree
        if current.right and not current.right.left and \
                             not current.right.right :
            return current.value

        current = current.right
