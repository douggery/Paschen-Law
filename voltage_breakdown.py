import control as ct
import seaborn
import matplotlib.pyplot as plt
import numpy as np

def v_breakdown(xdata,gamma):
	v=[np.float(100.*val/(np.log(val-np.log(np.log(1.+1./gamma))))) for val in xdata]
	return v

# pd=np.linspace(0,10,100)

for i in range(5):
	pd=np.linspace(0.1,20,1000)
	breakdowns=v_breakdown(pd,(1+i*2)*0.2)
	for k in range(len(breakdowns)):
		if breakdowns[k]>=0.0 and breakdowns[k-1]<=0.0:
			min_index=k
	breakdowns=breakdowns[min_index:-1]
	pd=pd[min_index:-1]
	plt.loglog(pd,breakdowns,label='Gamma = '+str(np.round((1+i*2)*0.1,0)))

plt.legend()
plt.xlabel('pressure*distance')
plt.ylabel('Fictional Breakdown Voltage')
plt.title('Theoretical Paschen Curves')
plt.show()