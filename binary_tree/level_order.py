class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

	"""
			30
		  /	   \
		25      35
		/ \     /  \
	 20     28  32   40
	"""
def insert(root, value):
	if(root is None):
		return Node(value)

	if(value > root.value):
		if (root.right is None):
			root.right = Node(value)
		else:	
			insert(root.right, value)

	else:
		if (root.left is None):
			root.left = Node(value)
		else:	
			insert(root.left, value)

def level_order_recurs(q):
	if len(q) == 0:
		return
	elements = len(q)
	for i in xrange(elements):
		node = q.pop(0)
		print node.value,
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	print "\n"		
	level_order_recurs(q)



root = Node(30)
insert(root, 25)
insert(root, 20)
insert(root, 28)
insert(root, 35)
insert(root, 32)
insert(root, 40)
q = []
q.append(root)
level_order_recurs(q)