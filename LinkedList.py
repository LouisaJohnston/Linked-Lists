# ## # ## # ## # ## 
# A single node of data in our list
class Node:
  # constructor
  def __init__(self, value):
    # value of the node
    self.value = value
    # reference to the next node
    self.next = None

  # Method override for printing
  # like __str__ but you can use any data type
  def __repr__(self):
    return f'{self.value}'

# test_node = Node('test string node')
# print(test_node)

# ## # ## # ## # ## 
# the linked list 'manager' class
class LinkedList:
  def __init__(self):
    # a reference to the head (first node)
    self.head = None
    # the current size of the linked list
    self.length = -1

  # helper function that checks if the linked list is empty
  def is_empty(self):
    return self.length == -1

  # add a node to the end of the list 
  def append(self, value):
    # create an end node from the given value
    new_node = Node(value)
    # check if the list is empty -- make new node the head if so
    if self.is_empty():
      self.head = new_node
    else:
      # loop to the end of the linked list
      # start at the beginning (the head node)
      current_node = self.head
      while current_node.next != None:
        current_node = current_node.next
      # set the last node's next to the new node
      current_node.next = new_node

    # increment the self.length
    self.length += 1
    return self.length

  # remove the last node and return it
  def pop(self):
    # check if the list is empty -- if so, return 'None'
    if self.is_empty(): return None

    # keep track of the previous node and current node while we loop
    previous_node = None
    current_node = self.head
    while current_node.next != None:
      # update the previous node
      previous_node = current_node
      # update the current node
      current_node = current_node.next
    # set the previous node's 'next' to be 'None'
    previous_node.next = None
    # decrease the self.length of the list
    self.length -= 1
    # return the node we removed 
    return current_node
  # print out our linked list
  def __repr__(self):
    # string to return
    list_string = ''
    # loop over the whole list
    # start at the head of the list
    current_node = self.head
    index = 0
    while current_node != None:
      # add the value of each node to the return string
      list_string += f'{index}: {current_node.value}\n'
      index += 1
      # go to the next node
      current_node = current_node.next

    # return the string
    return list_string

  # return the sum of all the values in the linked list
  def sum(self):
    node_sum = 0
    current_node = self.head
    while current_node != None:
      int_node = current_node.value
      node_sum += int_node
      current_node = current_node.next
    return node_sum

  # return a [list] (regular python list) from all the values in the linked list
  def to_list(self):
    node_list = []
    current_node = self.head
    while current_node != None:
      node_list.append(current_node.value)
      current_node = current_node.next
    return node_list

  # search for a given value in the list. 
  # If it is found, return True otherwise return False
  def search(self, value):
    pass
  
  # add a node with the given value to the beginning of the list
  # this doesn't need a loop -- remember the head is the beginning 
  # of the list. unshift should return the new length of the list
  def unshift(self, value):
    pass

  # remove the value at beginning of the list
  def shift(self):
    pass

