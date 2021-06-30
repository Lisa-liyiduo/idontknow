class Solution(object):
    def deleteDuplicates(self, head):
        if not head: return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        node=dummy.next
        while node:
            while node.next is not None and node.next.val==node.val:
                node=node.next
            if node==pre.next:
                pre=pre.next
            else:
                pre.next=node.next
            node=node.next
        return dummy.next
