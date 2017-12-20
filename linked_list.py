"""
Author: Jonathan Zwiebel
Version: 20 December 2017

An implementation of a linked list using a series of structs that point to eachother
Contains references to the front, back, and size of the list
Supports add(data), remove(data), contains(data), traverse()
"""

class linked_list_node:
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return str(self.data)

class linked_list:
	# Initializes a new blank linked_list
	# O(1)
	def __init__(self):
		self.front = None
		self.back = None
		self.size = 0

	# Adds a new node to the end of the linked_list
	# O(N)
	def add(self, data):
		new_node = linked_list_node(data)

		if self.size == 0:
			self.front = new_node
			self.back = new_node
		else:
			curr = self.front
			while curr.next_node != None:
				curr = curr.next_node
			curr.next_node = new_node
			self.back = new_node

		self.size += 1

	# Removes a node from the linked_list, returns whether the node was in the list
	# O(N)
	def remove(self, data):
		if self.size == 0:
			return False

		if self.size == 1:
			if self.front.data == data:
				self.front = None
				self.back = None
				self.size = 0
				return True
			else:
				return False

		if self.front.data == data:
			self.front = self.front.next_node
			self.size -= 1
			return True

		curr = self.front
		while curr.next_node != None:
			if curr.next_node.data == data:
				curr.next_node = curr.next_node.next_node
				if curr.next_node == None:
					self.back = curr
				self.size -= 1
				return True
			curr = curr.next_node
		return False

	# Returns whether the node was in the list
	# O(N)
	def contains(self, data):
		if self.size == 0:
			return False
		
		curr = self.front
		while curr != None:
			if curr.data == data:
				return True
			curr = curr.next_node
		return False


	# Gets the element at the specified index
	# O(N)
	def get(self, index):
		if index >= self.size:
			raise ValueError("List index out of bounds")
		n = 0
		curr = self.front
		while n < index:
			curr = curr.next_node
			n += 1 
		return curr.data

	# Inserts an element at the specified index
	# O(N)
	def insert(self, index, data):
		if index > self.size:
			raise ValueError("List index out of bounds")

		new_node = linked_list_node(data)
		self.size += 1

		if self.size == 1:
			self.front = new_node
			self.back = new_node

		elif index == 0:
			new_node.next_node = self.front
			self.front = new_node

		elif index == self.size - 1:
			self.back.next_node = new_node
			self.back = new_node

		else:
			n = 0
			curr = self.front
			while n < index - 1:
				curr = curr.next_node
				n += 1
			temp = curr.next_node
			curr.next_node = new_node
			new_node.next_node = temp

	# Removes the element at the given index
	# O(N)
	def remove_index(self, index):
		if index >= self.size:
			raise ValueError("List index out of bounds")

		self.size -= 1
		
		if self.size == 0:
			self.back = None

		if index == 0:
			self.front = self.front.next_node

		else:
			n = 0
			curr = self.front
			while n < index - 1:
				curr = curr.next_node
				n += 1
			if curr.next_node == self.back:
				curr.next_node = None
				self.back = curr
			else:
				curr.next_node = curr.next_node.next_node


	def join(self, other):
		if self.size == 0:
			self.front = other.front
			self.back = other.back
			self.size = other.size
		elif other.size != 0:
			self.back.next_node = other.front
			self.back = other.back
			self.size += other.size

	# Traverses the linked_list and returns a list of its values
	# O(N)
	def traverse(self):
		traversal = []
		curr = self.front
		while curr != None:
			traversal.append(curr.data)
			curr = curr.next_node
		return traversal


	# Prints the linked_list in order
	# O(N)
	def __str__(self):
		out = ""
		curr = self.front
		while curr != None:
			out += str(curr) + " "
			curr = curr.next_node
		return out