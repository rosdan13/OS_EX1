# OS 24 EX1
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Daniel Rosenzweig\Desktop\לימודים\OS\EX1\output.csv")
data = data.to_numpy()

l1_size = 65536
l2_size = 524288
l3_size = 16777216

plt.plot(data[:, 0], data[:, 1], label="Random access")
plt.plot(data[:, 0], data[:, 2], label="Sequential access")
plt.xscale('log')
#plt.yscale('log')
plt.axvline(x=l1_size, label="L1 (64 KB)", c='r')
plt.axvline(x=l2_size, label="L2 (512 KB)", c='g')
plt.axvline(x=l3_size, label="L3 (16 MB)", c='brown')
plt.legend()
plt.title("Latency as a function of array size on AMD Ryzen 9 6900HS")
plt.ylabel("Latency (ns)")
plt.xlabel("Bytes allocated (log scale)")
plt.show()
