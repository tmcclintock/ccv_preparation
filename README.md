# ccv_preparation
This is a collection of scripts needed to prepare SV and Y1 data 
for computing the CCV covariance matrices.

In order to run ccv you do:
./src/getmodel_g [output.fits] [zlens] [annuli_prefix] [zsource or p(z) prefix] [M200m/(h_^{-1}Msol)] ([cconc=1] [ccorr=5.0] [cell=3.7] [coff=0] [clss=0])

For zlens right now we are assuming z=0.24533 since we only have 
templates at the redshift for now. For the annuli prefix we can use 
thetas_z0_l0 for now. We only have pz for our p(z) prefix for now, 
but we will have one later for each redshift bin.
The amplitudes are unknown at the moment. For now we will use 
1 for everything.