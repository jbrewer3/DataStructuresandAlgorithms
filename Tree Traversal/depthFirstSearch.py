#calss to construct nodes
class Node():
    def __init__(self, value):
        self.value = value
        self.left =  None
        self.right = None
    
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items):
            return self.items.pop(0)

    def peek(self):
        if len(self.items):
            return self.items[0].value


class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, start, traversal): ##Root, Left, Right
        # Root -> Left -> Right
        if start is None:
            return

        traversal.append(start.value)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        return traversal

    def inorder(self, start, traversal):
        #Left -> Root -> Right
        if start is None:
            return

        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        #Left -> Right -> Root
        if start is None:
            return

        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)
        return traversal

    def levelorder(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue.items) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal



tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)


print(tree.preorder(tree.root, []))
print(tree.inorder(tree.root, []))
print(tree.postorder(tree.root, []))

print(tree.levelorder(tree.root))

''' 
                  [ 4 | 3 | 5 ]
                       /\
                      /  \
                     /    \ 
                    /      \ 
         [ 6 | 4 | 7 ]   [ 8 | 5 | 9 ]
                    
'''