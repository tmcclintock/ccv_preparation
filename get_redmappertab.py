"""
Create the redmapper.tab file.
"""
import numpy as np
Nz = 3
Nl = 7
line = "z%d %.2f pz annuli_z%d_l0\n"
outfile = open("redmapper.tab", "w")
path = "/home/tom/Desktop/DES_data/Y1_files/"
zs = np.loadtxt(path+"Y1_meanz.txt")

for i in range(Nz):
    z = zs[i, 0]
    outfile.write(line%(i, z, i))
outfile.close()
