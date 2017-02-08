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
					10						 

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

def path_sum(root, curr_sum, target, path):
	
	if root == None:
		return
	# print "at" + str(root.key) + " curr_ path = " + path
	if root.key == target:
		print root.key
	if curr_sum + root.key == target:
		path = path + " " + str(root.key)
		# print "desired sum found at" + str(root.key)
		print path
	elif curr_sum + root.key < target:
		path = path + " " + str(root.key)
		path_sum(root.left, curr_sum + root.key, target, path)
		# print str(root.key) + " completed left"
		path_sum(root.right, curr_sum + root.key, target, path)
		# print str(root.key) + " completed right"
	path_sum(root.left, 0, target, "")
	path_sum(root.right, 0, target, "")

root = Node(30)
insert(root, 25)
insert(root, 20)
insert(root, 28)
insert(root, 35)
insert(root, 32)
insert(root, 40)
insert(root, 10)
path_sum(root,0,0,"")