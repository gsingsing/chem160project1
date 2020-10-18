import numpy as np
import matplotlib.pyplot as plt
ntrials = 5000
N = 200
M = np.zeros(200)
for i in range(N):
    sum=0
    for j in range(ntrials):
        r = np.random.normal(0,1,N)
        m = np.max(r)
        sum += m
    Avg_Max = sum/ntrials
    M[i]=Avg_Max
plt.plot(range(1,201),M)
plt.xlabel("N")
plt.ylabel("Max Average")
plt.title("N distributed")