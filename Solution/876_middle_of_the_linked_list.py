class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val} -> {self.next}"

def middle_node(head: Node) -> Node:
    if not head:
        return None
    slow_ptr = fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(-6)
    head.next.next.next = Node(4)

    print(middle_node(head))