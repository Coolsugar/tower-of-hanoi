print("Starting Tower_of_Hanoi.py")
import time as t
num = int(input("Number of discs n = ")) #select number of discs
def TOH(n,source,dest,aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}.") #shift the nth disk to destination tower from source tower
    else:
        TOH(n-1,source,aux,dest) #shfting all n-1 disks to auxillary tower
        print(f"Move disk {n} from {source} to {dest}.") #shift nth disk to destination tower from source tower
        TOH(n-1,aux,dest,source) #shifting n-1 disks from auxillary tower back to desination treating source tower as new auxillary tower
t_start = t.time()
TOH(num,'A','B','C') #running function with selected number of disks, naming the towers
t_end = t.time()
print(f"Loop ended in {t_end - t_start:.5f} seconds.") #printing time taken for loop to run with a precison of 0.00001s.1
        