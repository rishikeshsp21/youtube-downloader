import os
import time
import re
path = "C:\\Users\\rishi\\Documents\\image processing outputs\\gan output images"
l = []
x = os.listdir(path)
x.sort()
print(len(x))
for i in range(len(x)):
    todelete = path +"\\" +  x[i]
    print(todelete)
    m = todelete.split()
    print(m)
    # a = re.search("24$", todelete) 
    # b = re.search("49$", todelete)
    # c = re.search("74$", todelete)
    # d = re.search("99$", todelete)
    # print(a, b, c, d)
    n = [m[-1]]
    print(n)
    n = n[0]
    print(n)
    n = n[:-4]
    print(n)
    if((int(n) + 1) % 25 != 0):
        print("deleted file: ", todelete)
        #os.remove(todelete)
    time.sleep(1)