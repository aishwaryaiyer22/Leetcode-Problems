import java.util.*;

class Node {
	char value;
	Node next;
	Node prev;

	public Node(char v) {
		value = v;
		next = null;
		prev = null;
	}
}

class Solution {
	public static void main(String args[]) {
		String input = "llmpoahc";
		boolean m = true;
		System.out.println(m);
		//single pass. maintain linked list of all non repeating characters. 
		//To have O(1) access to any element in linked list, maintain array of nodes. Perhaps use a hash table? 
		//dont really need a hash table as range of inputs is fixed. But lets try it with a hash table
		HashMap <Character, Node> chars_appeared = new HashMap<>();
		Node head,tail;
		int len = input.length();
		//initialize head and tail to first char of string
		head = new Node(input.charAt(0));
		tail = head;
		chars_appeared.put(new Character(input.charAt(0)),head);
		for(int i = 1; i< len; i++) {
			char curr_char = input.charAt(i);
			Character curr = new Character(curr_char);
			if(chars_appeared.containsKey(curr)) {
				Node n = chars_appeared.get(curr);
				if(head == n)
					head = head.next;
				else {
					n.prev.next = n.next;
				}
				if(tail == n)
					tail = n.prev;
				else
					n.next.prev = n.prev;
				n.prev = n.next = null;
				chars_appeared.put(curr,n);
			}
			else {
				Node n = new Node(curr_char);
				if(head == null) //tail will also be null
					head = tail = n;
				else {
					n.prev = tail;
					tail.next = n;
					tail = n;
				}
				chars_appeared.put(curr,n);
			}
		}
		if(head != null)
			System.out.println("First non repeating char is: "+head.value);
		else
			System.out.println("No non repeating chars found.");

	}
}