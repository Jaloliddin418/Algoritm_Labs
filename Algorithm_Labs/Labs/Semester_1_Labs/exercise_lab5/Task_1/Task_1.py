class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(parents):
    nodes = [TreeNode(i) for i in range(len(parents))]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
    return root

def tree_height(root):
    if not root:
        return 0
    if not root.children:
        return 1
    max_height = 0
    for child in root.children:
        max_height = max(max_height, tree_height(child))
    return max_height + 1

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        parents = list(map(int, f.readline().strip().split()))

    root = build_tree(parents)
    height = tree_height(root)

    with open('output.txt', 'w') as f:
        f.write(str(height))

if __name__ == "__main__":
    main()
