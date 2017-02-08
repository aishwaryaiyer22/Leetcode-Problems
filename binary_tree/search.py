class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

		"""
							30
						      /	   \
					            25      35
					          /   \	   /  \
					         20   28  32   40
"""

def insert(root, value):
	if(root is None):
		return Node(value)

	if(value > root.key):
		if (root.right is None):
			root.right = Node(value)
		else:	
			insert(root.right, value)

	else:
		if (root.left is None):
			root.left = Node(value)
		else:	
			insert(root.left, value)
	
def search(root, key):
	if(root is None or root.key == key):
		return root

	if(key < root.key):
		return search(root.left, key)
	else:
		return search(root.right, key)


def inorder(root):
	if (root):
		inorder(root.left)
		print root.key
		inorder(root.right)

root = Node(30)
insert(root, 25)
insert(root, 20)
insert(root, 28)
insert(root, 35)
insert(root, 32)
insert(root, 40)
inorder(root)
insert(root,33)
print "did 33 get inserted?"
inorder(root)
found = search(root, 33)
if found is not None:
	print "woho found {}".format(found.key)
else:
	print "not found"	
