class pro242 {
	public static void main(String[] args)
	{
		double N,T;
		double u1,u2,u3,Dt,k,E_exp,E_imp,E_CN;
	
		T = 5.0;
		N = 200.0;
		
		Dt = T/N;
	
		u1 = 1;
		u2 = 1;
		u3 = 1;
		
		for (int i = 1; i < N+1; i++) {
			u1 = u1 + u1*Dt;
			u2 = u2/(1-Dt);
			u3 = u3*(1+Dt*0.5)/(1-Dt*0.5);
		}
		k = Math.exp(T);
		System.out.println(u1);
		
	}	
	
}
		