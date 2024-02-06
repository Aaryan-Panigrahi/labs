class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):

	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)

	elif key > node.key:
		node.right = insert(node.right, key)

	return node


def inorder(root):
	if root is None:
		return

	inorder(root.left)
	print(root.key, end = " ")
	inorder(root.right)

def preorder(root):
	if root is None:
		return
	
	print(root.key, end = " ")
	preorder(root.left)
	preorder(root.right)

def postorder(root):
	if root is None:
		return
	
	postorder(root.left)
	postorder(root.right)
	print(root.key, end = " ")


if __name__ == "__main__":

	L = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

	root = None
	for i in range(len(L)):
		root = insert(root, L[i])

	print("Inorder - ")
	inorder(root)
	print("\n\nPreorder - ")
	preorder(root)
	print("\n\nPostorder - ")
	postorder(root)




