class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_at_tail(tail, data):
    new_node = Node(data)
    tail.next = new_node
    return new_node  # new tail


def insert_at_position(head, position, data):
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
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()
