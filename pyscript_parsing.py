import csv
import os
from pydoc import ispackage
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "CEA_tabulation_meth_400.txt")

# Turning tabulated CEA data into a list of lists
f =  open(filename)
lol = list(csv.reader(f, delimiter="\t"))
XD = []
for i in lol:    
    XD.append(i[0].split())

# print(tabulate(XD))

variables = XD.pop(0)

chamber = []
throat = []
exit = []

for i in range(len(XD)-1):
    
        if (i % 3) == 0: 
            chamber.append(XD[i])
        if (i % 3) == 1:
            throat.append(XD[i])
        if (i % 3) == 2: 
            exit.append(XD[i])

# print(tabulate(chamber))
# print(tabulate(throat))
# print(tabulate(exit))

# enter OF ratio range
OFratio = np.arange(1.5, 3.6, 0.1)
# OFratio = OFratio.reshape(20)
print(OFratio)
print(len(exit))
# print("chekc this aoualsdijf;laksjdf:")
# print("\n asdfalksjdflkajsdf")

if ("isp" in variables) or ("t" in variables):
    
    if "isp" in variables:
        
        isp = []
        isp_ind = variables.index("isp")
        for i in exit:
            isp.append(float(i[isp_ind])/9.8)
        # print("length isp: " + str(len(isp))+"\nlength  OF ratio: "+ str(len(OFratio)))
        print(isp)
        fig, ax1 = plt.subplots()
        color = 'tab:red'
        ax1.set_xlabel('OF ratio')
        ax1.set_ylabel('Isp (s)', color=color)
        ax1.plot(OFratio[0:20], isp[0:20], color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_title("Isp & chamber temperature")
    
    if "t" in variables:
        t = []
        t_ind = variables.index("t")
        for i in chamber:
            t.append(float(i[t_ind]))
        
        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('temperature (K)', color=color)  
        ax2.plot(OFratio, t, color=color)
        ax2.tick_params(axis='y', labelcolor=color)
    plt.show()

    



if "aeat" in variables:
    isp = []
    isp_ind = variables.index("aeat")
    for i in chamber:
        t.append(float(i[isp_ind])/9.8)
    plt.plot(OFratio,isp)
    plt.xlabel("OF ratio")
    plt.ylabel("Isp (s)")
    plt.title("Specific Impulse")
    plt.show()

aeat = []
isp = []
t = []

for i in exit:
    aeat.append(i[3])
    isp.append(i[1])

for i in chamber:
    t.append(float(i[4]))

