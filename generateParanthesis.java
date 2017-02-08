import java.util.*;

class genParan {
    public static void main(String args[]) {
        int n = 3;
        if(n == 0) {
            System.out.println("");
            return;
        }
        List<String> soln = new ArrayList<>();
        if(n == 1) {
            soln.add("()");
            System.out.println(soln);
            return;
        }
        generateUtil(soln, "", n, n);
        System.out.println(soln);
    }
    public static void generateUtil(List<String> soln, String curr, int opLeft, int closLeft) {
        if(opLeft == 0 && closLeft == 0){
            soln.add(curr);
        }
        else {
            if(opLeft == closLeft && opLeft > 0)
                generateUtil(soln, curr + '(', opLeft-1, closLeft);
            else if(opLeft > 0 && opLeft < closLeft) {
                generateUtil(soln, curr + '(', opLeft-1, closLeft);
                generateUtil(soln, curr + ')', opLeft, closLeft-1);
            }
            else if(opLeft == 0)
                 generateUtil(soln, curr + ')', opLeft, closLeft-1);
        }
    }
}