class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sortedArrayToBST(arr, start, end):

    if start > end:
        return None

    mid = start + (end - start) // 2

    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr, start, mid - 1)

    root.right = sortedArrayToBST(arr, mid + 1, end)

    return root


def printTree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (4 * level) + prefix + str(root.data))
        printTree(root.left, level + 1, prefix="L--- ")
        printTree(root.right, level + 1, prefix="R--- ")


arr = [0, 1, 2, 3, 4]
root = sortedArrayToBST(arr, 0, len(arr) - 1)
printTree(root)
