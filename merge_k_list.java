import java.util.*;
import java.io.*;
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
 }
 

class Merge {

    public static void main(String[] args) {
        System.out.println(mergeKLists(null));
    }
    public static ListNode mergeKLists(ListNode[] lists) {
        
        if (lists == null)
            return null;
        if (lists.length == 1)
            return lists[0];
        PriorityQueue<ListNode> minHeap = new PriorityQueue(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode h1, ListNode h2) {
                return h1.val-h2.val;
            }
        });
        ListNode sortedList = new ListNode(-1);
        for(int i =0; i < lists.length; i++) {
            minHeap.add(lists[i]);
        }
        ListNode sortedPtr = sortedList;
        ListNode top;
        while(minHeap.size() != 0) {
            top = minHeap.poll();
            sortedPtr.next = top;
            if(top.next != null) {
                minHeap.add(top.next);
                top.next = null;
            }
            sortedPtr = sortedPtr.next;
        }
        return sortedList.next;
    }
}