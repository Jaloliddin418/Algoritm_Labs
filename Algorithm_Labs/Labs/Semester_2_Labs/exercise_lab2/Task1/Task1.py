class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = TreeNode(key)
            node.size += 1
        elif key > node.key:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = TreeNode(key)
            node.size += 1

    def kth_smallest(self, k):
        return self._kth_smallest(self.root, k)

    def _kth_smallest(self, node, k):
        left_size = node.left.size if node.left else 0

        if k == left_size + 1:
            return node.key
        elif k <= left_size:
            return self._kth_smallest(node.left, k)
        else:
            return self._kth_smallest(node.right, k - left_size - 1)

with open('input.txt', 'r') as file:
    lines = file.readlines()

bst = BST()
results = []

for line in lines:
    if line.startswith('+'):
        _, x = line.split()
        x = int(x)
        bst.insert(x)
    elif line.startswith('?'):
        _, k = line.split()
        k = int(k)
        results.append(bst.kth_smallest(k))

with open('output.txt', 'w') as file:
    for result in results:
        file.write(f"{result}\n")
