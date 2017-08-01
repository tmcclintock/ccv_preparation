"""
A script for running ccv.
"""
import numpy as np
import os, sys

path = "/home/tom/Desktop/DES_data/Y1_files/"
zs = np.loadtxt(path+"Y1_meanz.txt")
lams = np.loadtxt(path+"Y1_meanl.txt")
number = np.loadtxt(path+"Y1_number.txt")
Nz = len(zs)
Nl = len(zs[0])
masses = np.loadtxt("../ccv_preparation/masses.txt")
theta_path = "../ccv_preparation/theta_files/theta_z%d_l%d.tab"

#Command out_path zlens annuli_prefix zsource 
command = "./src/getmodel_ds outfiles/output_z%d_l%d %.5f theta_z%d_l%d 1.0 %e 0 5.0 3.7 0 0"

for i in range(Nz):
    for j in range(Nl):
        #os.system("cp %s ."%theta_path%(i,j))
        mass = masses[i, j]
        z = zs[i, j]
        this_command = command%(i, j, z, i, j, mass)
        print "Running: %s"%this_command
        #os.system(this_command)
