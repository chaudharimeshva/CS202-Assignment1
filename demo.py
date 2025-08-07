"""This code is showing the basic understanding of Linklist data structure"""

class Node:
   # pylint: disable=too-few-public-methods
    def __init__(self, data):
       """Initialising data and next pointer."""
        self.data = data
        self.next = None


def insert_at_head(head, data):
    """Insert a new node with the given data at the head of the list."""
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_at_tail(tail, data):
    """Insert a new node with the given data at the tail of the list."""
    new_node = Node(data)
    tail.next = new_node
    return new_node  # new tail


def insert_at_position(head, position, data):
    """Insert a new node at the Perticular location."""
    if position == 1:
        return insert_at_head(head, data)

    temp = head
    count = 1

    while count < position - 1 and temp is not None:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of bounds.")
        return head

    new_node = Node(data)
    new_node.next = temp.next
    temp.next = new_node
    return head


def delete_node(head, position):
    """Deleting a new node with the given data at the head of the list."""
    if head is None:
        print("List is empty")
        return None

    if position == 1:
        temp = head
        head = head.next
        del temp
        return head

    curr = head
    prev = None
    count = 1

    while count < position and curr is not None:
        prev = curr
        curr = curr.next
        count += 1

    if curr is None:
        print("Position out of bounds")
        return head

    prev.next = curr.next
    del curr
    return head


def print_list(head):
    """Printing the lins."""
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()
