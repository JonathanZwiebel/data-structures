
def test_traverse():
	"""
	Case 1: List empty
	Case 2: List non-empty
	"""
	list_ = linked_list()
	assert list_.traverse() == []
	list_.add(3)
	assert list_.traverse() == [3]
	print("traverse() method passes")

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
	print("add() method passes")

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
	print("remove() method passes")

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
	print("contains() method passes")

test_traverse()
test_add()
test_remove()
test_contains()