from matplotlib.pylab import *
class solver:
	def __init__(self,f,u0,T,N):
		self.f = f
		self.T = T
		self.N = N
		self.u0 = u0
		self.u = zeros(N+1)
		self.t = linspace(0,T,N+1)
		self.dt = float(T)/N
	
	def solve(self):
		self.u[0] = self.u0	
		for n in range(self.N):
			self.u[n+1] = self.step(self.u[n],self.t[n])
	
		return self.u,self.t

	
	def error(self,u_ex):
		return abs(u_ex(self.T)-self.u[-1])
	

class FE(solver):
	def step(self,u_,t):
		u = u_ + self.dt*self.f(u_,t)
		return u
	
class Heun(solver):
	def step(self,u_,t):
		F1 = self.f(u_,t)
		F2 = self.f(u_ + self.dt*F1,t+self.dt)
	
		u = u_ + 0.5*self.dt*(F1+F2)
		return u
class RK4(solver):
	def step(self,u_,t):
		f = self.f
		F1 = f(u_,t)
		F2 = f(u_ + 0.5*self.dt*F1,t+0.5*self.dt)
		F3 = f(u_ + 0.5*self.dt*F2,t+0.5*self.dt)
		F4 = f(u_ + self.dt*F3,t+self.dt)
		u = u_ + (self.dt/6.0)*(F1+2*F2+2*F3+F4)
		return u


T = 2.0

eps = 0.5
f = lambda u,t: 2*(1-t)*u/eps**2
u0 = exp(-1/eps**2)
err = 10
u_ex = lambda t: u0*exp((2-t)*t/eps**2)
'''

f = lambda u,t: u*(1-u)



u0 = 10
solver = RK4(f,u0,T,100)
u,t = solver.solve()
u_ex = exp(t)*(exp(t)-0.9)**-1
plot(t,u)
show()
'''

i = 1
import time
while err > 1E-5:
	N = 10*2**i
	solver = Heun(f,u0,T,N)
	t1 = time.time()
	solver.solve()
	time_used = time.time()-t1
	err = solver.error(u_ex)
	i *= 2
	print err, time_used
	
	
	#plot(t,u,t,exp(-((1-t)/eps)**2))
	#show()