class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val} -> {self.next}"

def delete_node(head: Node, node):
    ptr = head
    while ptr:
        if ptr.val == node:
            ptr.val = ptr.next.val
            ptr.next = ptr.next.next
            break
        ptr = ptr.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(-6)
    head.next.next.next = Node(4)

    print(delete_node(head, 3))
    print(head)