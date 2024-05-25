class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(nodes_info):
    nodes = [None] * (len(nodes_info) + 1)
    for i, (key, left, right) in enumerate(nodes_info):
        if nodes[i + 1] is None:
            nodes[i + 1] = TreeNode(key)
        nodes[i + 1].key = key
        if left != 0:
            nodes[i + 1].left = nodes[left] if nodes[left] else TreeNode(None)
            nodes[left] = nodes[i + 1].left
        if right != 0:
            nodes[i + 1].right = nodes[right] if nodes[right] else TreeNode(None)
            nodes[right] = nodes[i + 1].right
    return nodes[1]  # root node

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def delete_subtree(root, key):
    if not root:
        return None, 0
    if key < root.key:
        root.left, removed_count = delete_subtree(root.left, key)
    elif key > root.key:
        root.right, removed_count = delete_subtree(root.right, key)
    else:
        removed_count = count_nodes(root)
        return None, removed_count
    return root, removed_count

def process_deletions(root, deletions):
    remaining_nodes = count_nodes(root)
    results = []
    for key in deletions:
        root, removed_count = delete_subtree(root, key)
        remaining_nodes -= removed_count
        results.append(remaining_nodes)
    return results

with open('input.txt', 'r') as file:
    N = int(file.readline().strip())
    nodes_info = [tuple(map(int, file.readline().strip().split())) for _ in range(N)]
    M = int(file.readline().strip())
    deletions = list(map(int, file.readline().strip().split()))

root = build_tree(nodes_info)

results = process_deletions(root, deletions)

with open('output.txt', 'w') as file:
    for result in results:
        file.write(f"{result}\n")
