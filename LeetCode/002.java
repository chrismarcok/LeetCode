/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.math.BigInteger;
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode curNode = l1;
        String num1 = "";
        while (curNode != null){
            num1 = String.valueOf(curNode.val) + num1;
            curNode = curNode.next;
        }
        curNode = l2;
        String num2 = "";
        while (curNode != null){
            num2 = String.valueOf(curNode.val) + num2;
            curNode = curNode.next;
        }
        BigInteger n1 = new BigInteger(num1);
        BigInteger n2 = new BigInteger(num2);
        String result = String.valueOf(n2.add(n1));
        
        //result is "807". want 7 -> 0 -> 8
        
        ListNode prevNode = new ListNode(0);
        ListNode resultNode = new ListNode(0);
        
        for(int i = result.length() - 1; i >= 0; i--){
            
            curNode = new ListNode(Integer.parseInt("" + result.charAt(i)));
            
            if (i== result.length()-1){
                resultNode = curNode;
            }
            prevNode.next = curNode;
            prevNode = curNode;
        }
        return resultNode;
        
    }
}