"""
Take radial bins and convert them to arcminutes
in a .tab file structured the way that we need
in order to use it in the ccv repository.
"""
import numpy as np
from scipy.integrate import quad

c = 2.99792e5 #km/s; speed of light
radians_per_am = np.pi/10800. #radians per arcminute

#The cosmology
h = 0.7
H0 = h*100. #km/s/Mpc
Omega_m = 0.3
Omega_l = 0.7
Omega_k = 0.0

#Redshift
z=1.0

# Angular diameter distance, a physical distance; Mpc
def calc_DA(z,H0,Om,Ol):
    def integrand(z,Om,Ol):
        return 1./np.sqrt(Om*(1+z)**3+Ol)
    da = quad(integrand,0,z,args=(Om,Ol))[0]
    return (c/H0)*da/(1+z)
    
#Define the radial bin edges
bmin = 0.02 #Mpc physical
bmax = 30.0 #Mpc physical
lbmin = np.log(bmin)
lbmax = np.log(bmax)
R = np.exp(np.linspace(lbmin,lbmax,15))
DA = calc_DA(z,H0,Omega_m,Omega_l) #Mpc physical
theta = R/DA/radians_per_am #arcminutes
theta_bins = np.array([theta[:-1],theta[1:]]).T
R_bins = np.array([R[:-1],R[1:]]).T
print theta_bins

#Write to a file
prefix = "thetas_z0_l0"
outfile = open(prefix+".tab","w")
outfile.write("%d\n"%len(theta_bins))
for i in range(len(theta_bins)):
    outfile.write("%.4f %.4f\n"%(theta_bins[i,0],theta_bins[i,1]))
outfile.close()