class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def min_height(root):
    if root == None:
        return 0
    ldepth = min_height(root.left)
    rdepth = min_height(root.right)

    if ldepth > rdepth:
        return (1+rdepth)
    else:
        return 1+ldepth


root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.right=Node(7)


print(min_height(root))
