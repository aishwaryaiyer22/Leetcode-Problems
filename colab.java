import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Solution {
    public static void main(String args[]) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine();
        String line1_words[] = line1.split(" ");
        if(line1_words.length != 2){
                System.out.println("Invalid input");
                return;
        }
        int m = Integer.parseInt(line1_words[1]);
        int n = Integer.parseInt(line1_words[0]);
        int a,b,c;
        ArrayList <Integer> cards = new ArrayList<>();
        ArrayList <String[]> operations = new ArrayList<>();
        
        for(int i = 1; i <= m; i++) {
            String t = sc.nextLine();
            operations.add(t.split(" "));
            System.out.println(t);
        }
            
        for(int i = 1; i <= n; i++)
            cards.add(i);
        System.out.println(cards);     
        for(String [] op : operations) {
            if(op.length != 3 ){
                System.out.println("Invalid input");
                return;
            }
               
            a = Integer.parseInt(op[0]);
            b = Integer.parseInt(op[1]);
            c = Integer.parseInt(op[2]);
           
            System.out.println(a + "" + b + "" + c);
            ArrayList<Integer> tmp = new ArrayList(cards.subList(a,a+b));
            cards.removeAll(tmp);
            System.out.println(cards);
            Collections.reverse(tmp);
            if(c >= 0 && c <= cards.size())
                cards.addAll(c,tmp);
            else
                System.out.println("Invalid insertion index");
            System.out.println(cards);
        }
        System.out.println(cards);
    }
}