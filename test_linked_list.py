from linked_list import linked_list

def test_traverse():
	"""
	Case 1: List empty
	Case 2: List non-empty
	"""
	list_ = linked_list()
	assert list_.traverse() == []
	list_.add(3)
	assert list_.traverse() == [3]

def test_add():
	"""
	Case 1: List empty
	Case 2: List non-empty
	"""
	list_ = linked_list()
	list_.add(3)
	assert list_.traverse() == [3] and list_.size == 1 and list_.front.data == 3 and list_.back.data == 3
	list_.add(5)
	assert list_.traverse() == [3, 5] and list_.size == 2 and list_.front.data == 3 and list_.back.data == 5

def test_remove():
	"""
	Case 1: List empty
	Case 2: Single element, contains
	Case 3: Single element, does not contain
	Case 4: Multiple elements, at front
	Case 5: Multiple elements, in middle
	Case 6: Multiple elements, at back
	Case 7: Multiple elements, does not contain
	"""
	list_ = linked_list()
	assert list_.remove(1) == False
	list_.add(2)
	assert list_.remove(2) == True
	assert list_.traverse() == [] and list_.size == 0 and list_.front == None and list_.back == None
	list_.add(3)
	assert list_.remove(4) == False
	assert list_.traverse() == [3] and list_.size == 1 and list_.front.data == 3 and list_.back.data == 3
	list_.add(4)
	assert list_.remove(3) == True
	assert list_.traverse() == [4] and list_.size == 1 and list_.front.data == 4 and list_.back.data == 4
	list_.add(5)
	list_.add(6)
	assert list_.remove(5) == True
	assert list_.traverse() == [4, 6] and list_.size == 2 and list_.front.data == 4 and list_.back.data == 6
	assert list_.remove(6) == True
	assert list_.traverse() == [4] and list_.size == 1 and list_.front.data == 4 and list_.back.data == 4
	list_.add(7)
	assert list_.remove(8) == False
	assert list_.traverse() == [4, 7] and list_.size == 2 and list_.front.data == 4 and list_.back.data == 7

def test_contains():
	"""
	Case 1: List empty
	Case 2: Contains front
	Case 3: Contains middle
	Case 4: Contains back
	Case 5: Does not contain
	"""
	list_ = linked_list()
	assert list_.contains(1) == False
	list_.add(2)
	list_.add(3)
	list_.add(4)
	assert list_.contains(2) == True
	assert list_.contains(3) == True
	assert list_.contains(4) == True
	assert list_.contains(5) == False

def test_get():
	"""
	Case 1: List empty
	Case 2: Index 0
	Case 3: Middle index
	Case 4: Last index 
	Case 5: Out of bounds index
	"""
	list_ = linked_list()
	caught = False
	try:
		list_.get(1)
	except ValueError:
		caught = True
	assert caught
	caught = False
	list_.add(2)
	list_.add(3)
	list_.add(4)
	assert list_.get(0) == 2
	assert list_.get(1) == 3
	assert list_.get(2) == 4
	try:
		list_.get(3)
	except ValueError:
		caught = True
	assert caught

def test_insert():
	"""
	Case 1: List empty out of bounds
	Case 2: List empty
	Case 3: Single element start
	Case 4: Single element ends
	Case 5: Multiple element start
	Case 6: Multiple element middle
	Case 7: Multiple element end
	Case 8: Out of bounds
	"""
	list_ = linked_list()
	caught = False
	try:
		list_.insert(1, 1)
	except ValueError:
		caught = True
	assert caught
	list_.insert(0, 1)
	assert list_.traverse() == [1] and list_.size == 1 and list_.front.data == 1 and list_.back.data == 1
	list_.insert(0, 2)
	assert list_.traverse() == [2, 1] and list_.size == 2 and list_.front.data == 2 and list_.back.data == 1
	list_.remove(2)
	list_.insert(1, 2)
	assert list_.traverse() == [1, 2] and list_.size == 2 and list_.front.data == 1 and list_.back.data == 2
	list_.insert(0, 3)
	assert list_.traverse() == [3, 1, 2] and list_.size == 3 and list_.front.data == 3 and list_.back.data == 2
	list_.insert(2, 4)
	assert list_.traverse() == [3, 1, 4, 2] and list_.size == 4 and list_.front.data == 3 and list_.back.data == 2
	list_.insert(4, 5)
	assert list_.traverse() == [3, 1, 4, 2, 5] and list_.size == 5 and list_.front.data == 3 and list_.back.data == 5
	caught = False
	try:
		list_.insert(6, 6)
	except ValueError:
		caught = True
	assert caught and list_.traverse() == [3, 1, 4, 2, 5] and list_.size == 5 and list_.front.data == 3 and list_.back.data == 5

def test_remove_index():
	"""
	Case 1: List empty
	Case 2: Single element
	Case 3: Multiple element front
	Case 4: Multiple element back
	Case 5: Multiple element middle
	Case 6: Out of bounds
	"""
	list_ = linked_list()
	caught = False
	try:
		list_.remove_index(0)
	except ValueError:
		caught = True
	assert caught
	list_.add(1)
	list_.remove_index(0)
	assert list_.traverse() == [] and list_.size == 0 and list_.front == None and list_.back == None
	list_.add(2)
	list_.add(3)
	list_.add(4)
	list_.add(5)
	list_.remove_index(0)
	assert list_.traverse() == [3, 4, 5] and list_.size == 3 and list_.front.data == 3 and list_.back.data == 5
	list_.remove_index(1)
	assert list_.traverse() == [3, 5] and list_.size == 2 and list_.front.data == 3 and list_.back.data == 5
	list_.remove_index(1)
	assert list_.traverse() == [3] and list_.size == 1 and list_.front.data == 3 and list_.back.data == 3
	caught = False
	try:
		list_.remove_index(1)
	except ValueError:
		caught = True
	assert caught

def test_join():
	"""
	Case 1: Both lists empty
	Case 2: List A empty
	Case 3: List B empty
	Case 4: Both lists normal
	"""	
	list_a = linked_list()
	list_b = linked_list()
	list_a.join(list_b)
	assert list_a.traverse() == [] and list_a.size == 0 and list_a.front == None and list_a.back == None
	list_c = linked_list()
	list_c.add(1)
	list_c.add(2)
	list_c.add(3)
	list_a.join(list_c)
	assert list_a.traverse() == [1, 2, 3] and list_a.size == 3 and list_a.front.data == 1 and list_a.back.data == 3
	list_d = linked_list()
	list_a.join(list_d)
	assert list_a.traverse() == [1, 2, 3] and list_a.size == 3 and list_a.front.data == 1 and list_a.back.data == 3
	list_e = linked_list()
	list_e.add(4)
	list_e.add(5)
	list_e.add(6)
	list_a.join(list_e)
	assert list_a.traverse() == [1, 2, 3, 4, 5, 6] and list_a.size == 6 and list_a.front.data == 1 and list_a.back.data == 6

def test_linked_list():
	try:
		test_traverse()
		test_add()
		test_remove()
		test_contains()
		test_get()
		test_insert()
		test_remove_index()
		test_join()
	except AssertionError:
		print("Linked list failed")
	else:
		print("Linked list passed")

test_linked_list()