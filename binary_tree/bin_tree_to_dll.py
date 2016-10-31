class Node :
	def __init__(self, key):
		self.left = null
		self.right = null
		self.key = key
		
def listify(Node root):
	if root is None:
            return (None, None)

        (left_first, left_last) = listify(root.left)
        (right_first, right_last) = listify(root.right)

        first = last = root

        if left_last:
            left_last.right = root
            root.left = left_last
            first = left_first

        if right_first:
            right_first.left = root
            root.right = right_first
            last = right_last

        return (first, last)
