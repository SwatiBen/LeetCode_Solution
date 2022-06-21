// # 2 . Add two numbers
// # You are given two non-empty linked lists representing two non-negative integers. 
// # The digits are stored in reverse order, and each of their nodes contains a single digit. 
// # Add the two numbers and return the sum as a linked list.
// # You may assume the two numbers do not contain any leading zero, except the number 0 itself.


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first = l1, second = l2;
        int carry = 0;
        ListNode dummy = new ListNode(0);
        ListNode trav = dummy;
        while(first != null || second != null || carry!= 0){
            if (first != null){
                carry += first.val;
                first = first.next;
            }
            if (second != null){
                carry +=second.val;
                second = second.next;
            }
            
            trav.next = new ListNode(carry % 10);
            trav = trav.next;
            carry /=10;
            }
        
        return dummy.next;
    }
}