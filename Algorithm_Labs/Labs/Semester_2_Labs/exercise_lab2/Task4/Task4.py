# Задание 11
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def balance_node(self, node):
        self.update_height(node)
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node
        return self.balance_node(node)

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        return self.balance_node(node)

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def exists(self, node, key):
        if not node:
            return False
        if key < node.key:
            return self.exists(node.left, key)
        elif key > node.key:
            return self.exists(node.right, key)
        else:
            return True

    def next(self, node, key):
        successor = None
        while node:
            if key < node.key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor

    def prev(self, node, key):
        predecessor = None
        while node:
            if key > node.key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def exists_key(self, key):
        return self.exists(self.root, key)

    def next_key(self, key):
        node = self.next(self.root, key)
        return node.key if node else None

    def prev_key(self, key):
        node = self.prev(self.root, key)
        return node.key if node else None

# Чтение входных данных
with open('input.txt', 'r') as file:
    operations = [line.strip() for line in file]

avl_tree = AVLTree()
results = []

for operation in operations:
    command = operation.split()
    op = command[0]
    x = int(command[1])

    if op == "insert":
        avl_tree.insert_key(x)
    elif op == "delete":
        avl_tree.delete_key(x)
    elif op == "exists":
        result = "true" if avl_tree.exists_key(x) else "false"
        results.append(result)
    elif op == "next":
        result = avl_tree.next_key(x)
        results.append(str(result) if result is not None else "none")
    elif op == "prev":
        result = avl_tree.prev_key(x)
        results.append(str(result) if result is not None else "none")

# Запись результатов
with open('output.txt', 'w') as file:
    for result in results:
        file.write(result + "\n")
