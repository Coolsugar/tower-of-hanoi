print("Time_TOH.py is starting...")
import time as t
import matplotlib.pyplot as plt
record = {} #empty dictionary
number = int(input("Select maximum integral value for number of discs to be timed: "))
def TOH(n,source,dest,aux):
    if n == 1:
        pass
        #print(f"Move disk 1 from {source} to {dest}.") #shift the nth disk to destination tower from source tower SILENCED
    else:
        TOH(n-1,source,aux,dest) #shfting all n-1 disks to auxillary tower
        #print(f"Move disk {n} from {source} to {dest}.") #shift nth disk to destination tower from source tower SILENCED
        TOH(n-1,aux,dest,source) #shifting n-1 disks from auxillary tower back to desination treating source tower as new auxillary tower
def time(n): #running TOH for n value = n
    start_time = t.time() #recording start and end times
    TOH(n,'A','B','C')
    end_time = t.time()
    return end_time - start_time
tao_start = t.time()   
for n in range(1,number+1): #running TOH for every inetgral value from 1 to n
    rec_time = time(n)
    record[n] = rec_time
    print(record)

print("Ended with results: ")
print(record)

print("Graphing results...")
x = []
y = []
plt.xlabel("Integral Value (number of disks)")
plt.ylabel("Time Taken")
plt.title(f"Observing Exponential Computaion in TOH. \n Maximum number of disks N = {number}")
plt.grid()
for key , value in record.items():
    x.append(key)
    y.append(value)
plt.plot(x,y, label='', color='blue')
tao_end = t.time()
print(f"Entire program ended in {tao_end - tao_start:2f} seconds.")

#matching estimation:
import math
import numpy as np
X = np.linspace(0,30,10000)
e = math.e
def f(X):
    Y = (3.883064922345016e-11)*(e**X) + 0.7282940499733179
    return Y 
plt.plot(X , f(X), label='f(x)', color='red')
plt.show()