from tqdm import tqdm
import matplotlib.pyplot as plt

storage = {}

for integer in tqdm(range(100000,1000000),desc="Calculating...") :
    square = list(str(integer ** 2))
    square.reverse()
    num = ""
    for position in range(4,7):
        num =  square[position] + num
    num = int(num)
    
    if num not in storage:
        storage[num] = 0
    
    storage[num]+=1
    
sorted(storage)


total = 0
for key in storage:
    total += storage[key]-1

mean = int(total/len(storage))
sorted_keys = sorted(storage.keys())
max_crash, min_crash = sorted_keys[0], sorted_keys[len(sorted_keys)-1]
max_value, min_value = storage[max_crash], storage[min_crash]



out = "Total number of unique hashvalues was %s \nThe average amount of collisions for a arbritary hashvalue was %s \nThe hash that crashed the most was %s with %s crashes \nThe hash that crashed the least was %s with %s crashes"%(len(storage),mean,max_crash,max_value,min_crash,min_value)
print(out)