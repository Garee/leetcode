/**
 * 206. Reverse Linked List (Easy)
 *
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 *
 * Constraints
 *
 *   The number of nodes in the list is the range [0, 5000].
 *   -5000 <= Node.val <= 5000
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    let curr = head;
    let prev = null;

    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
};

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

test("example 1", () => {
    const list = ListNode();
    const ans = reverseList(list);
    expect(ans).toBeDefined();
});
