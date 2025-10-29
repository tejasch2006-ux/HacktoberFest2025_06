class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_palindrome(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]
