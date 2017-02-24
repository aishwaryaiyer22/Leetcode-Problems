class WaysToReach {
	public static void main(String args[]) {
		int n = 610;
		long [] steps = new long[n+1];
		long result = count(n, steps);
		System.out.println("Result "+result);
	}
	public static long count(int n, long [] steps) {
		if(n == 0)
			return 1;
		if(steps[n] != 0) {
			//System.out.println("n and its val are "+n +" " + steps[n]);
			return steps[n];
		}		
			
		long k = 0;
		for(int i = 1; i <= 6; i++) {
			if(n-i < 0)
				break;
			k += count(n-i, steps);
		}
		steps[n] = k;
		System.out.println("n and its val are "+n +" " + steps[n]);
		return k;
	}
}