def reverseLink(head):
    if len(head) == 1:
        return head
    if not head:
        return []
    return reverseLink(head[1:]) + [head[0]]

print(reverseLink([1,2,3,4]))