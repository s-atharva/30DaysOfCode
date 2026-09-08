def find_diameter(node):
    if node is None:
        return 0
    left = find_diameter(node.left)
    right = find_diameter(node.right)
    diameter = max(diameter, left + right)
    return 1 + max(left, right)
