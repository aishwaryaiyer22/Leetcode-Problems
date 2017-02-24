import java.util.*;
class Solution {

	final static double sqFive = Math.sqrt(5);
	static double findNth(int n) {
		/*Using binets formula*/
		double result = (1/sqFive) * (Math.pow((1 + sqFive) / 2, n) - Math.pow((1 - sqFive)/2, n));
		return result; 
	}

	public static void main(String args[]) {
		/*Given an n, find f(n) where f(n) = f(n-1) + f(n-2)*/
		int n = 8181;
		double result = findNth(n);
		System.out.println(result);
	}
}