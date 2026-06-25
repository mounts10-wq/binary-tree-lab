from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth of a binary tree.

    The depth is the number of nodes along the longest path
    from the root down to the farthest leaf node.
    """
    # Base case: empty tree has depth 0
    if root is None:
        return 0

    # Recursively compute the depth of each subtree
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # The total depth is the larger subtree depth plus the current node
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Returns the lowest common ancestor of nodes p and q in a BST.

    Uses BST ordering:
    - If both values are smaller than root, search left.
    - If both values are greater than root, search right.
    - Otherwise, root is the lowest common ancestor.
    """
    # If both target nodes are in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # If both target nodes are in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # If they split here (or one equals root), root is the LCA
    return root
