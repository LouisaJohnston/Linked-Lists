# ## # ## # ## # ##
# testing area for our linked list
from LinkedList import LinkedList

our_list = LinkedList()

our_list.append(1)
our_list.append(1)
our_list.append(3)
our_list.append(42)
our_list.append(1003)
our_list.append(67)

# print('before pop', our_list)

# our_list.pop()

# print('after pop', our_list)

print(our_list.sum())