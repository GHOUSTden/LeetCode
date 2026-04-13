class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}"

def has_cycle(head: Node) -> bool:
    slow_ptr = fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            slow_ptr = head
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return slow_ptr

if __name__ == "__main__":
    head = Node(1)
    cycle_node = head.next = Node(2)
    head.next.next = cycle_node

    print(has_cycle(head))