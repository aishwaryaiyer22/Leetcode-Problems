import java.util.*;

class Surpasser {
	public static void main(String args[]) {
		int input[] = {2,7,5,3,0,8,1};
		//int count[] = new int[10000];
		//lets do brute force shall we
		int result[] = new int[input.length];
		int curr,res;
		for(int i = 0;i < input.length-1; i++) {
			curr = input[i];
			res = 0;
			for(int j = i+1; j < input.length; j++) {
				if(input[j] > curr)
					res++;
			}
			result[i] = res;
		}
		for(int i = 0;i < input.length; i++)
			System.out.print(result[i]+" ");

		//now to optimize......
	}
}