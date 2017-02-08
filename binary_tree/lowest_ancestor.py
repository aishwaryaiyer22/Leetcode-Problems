class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

		"""
							30
						  /	   \
					    25      35
					    /\     /  \
					  20  28  32   40
					  /\  /\  /\   /\
					 5  6 7 8

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

def lowest_ancestor(root, p, q,v):
	if root == None:
		return None
	if root.key == p:
		v[0] = True 
		return root
	if root.key == q:
		v[1] = True
		return root
	onLeft = lowest_ancestor(root.left, p ,q, v)
	onRight = lowest_ancestor(root.right, p ,q, v)

	if onLeft != None and onRight != None:
		return root
	elif onLeft == None:
		return onRight
	else: 
		return onLeft

root = Node(30)
insert(root, 25)
insert(root, 20)
insert(root, 28)
insert(root, 35)
insert(root, 32)
insert(root, 40)
v = [False] * 2
res = lowest_ancestor(root, 32, 90, v)
if res != None and v[0] == True and v[1] == True:
	print res.key
else:
	print "Null"	
