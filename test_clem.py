#combinaison

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time
import csv


# ------------------------------
# Data Declarations
# ------------------------------
R_min = 0.75  # Rayons interieur de la couronne en cm
R_max = 1  # Rayons exterieur de la couronne en cm
Z = 39  # Numéro atomique Yttrium
# Z = 55  # Numéro atomique Cesium
Energie_coupure = 2.00000E-03  # MeV

# Energies des différents photons emis suite à la desintégration
E_pho_100 = 1.0000E-01  # MeV
E_pho_50 = 5.00000E-02  # MeV
E_pho_30 = 3.00000E-02  # MeV
E_pho_10 = 1.00000E-02  # MeV

# Intensités relatives (Normalizées)
P_pho_100 = 0.20  # Proba parmis les 4 Energies de photons émis qu'un photon de 100 kev soit émis
P_pho_50 = 0.30  # Proba parmis les 4 Energies de photons émis qu'un photon de 50 kev soit émis
P_pho_30 = 0.35  # Proba parmis les 4 Energies de photons émis qu'un photon de 30 kev soit émis
P_pho_10 = 0.15  # Proba parmis les 4 Energies de photons émis qu'un photon de 10 kev soit émis

# Nombre de particules
N = 100  ####### DANS UN PREMIER TEMPS TESTONS AVEC UN FAIBLE NOMBRE DE PHOTONS

# DONNÉES INTERPOLATION (Photons) POUR BLOC D

#Energies pour l'axe des x (abscisse) du Cs (MeV)
energie_Cs = np.array([1.00000E-03,1.03199E-03,1.06500E-03,1.06500E-03,1.13851E-03,
                       1.21710E-03,1.21710E-03,1.50000E-03,2.00000E-03,3.00000E-03,
                       4.00000E-03,5.00000E-03,5.01190E-03,5.01190E-03,5.18274E-03,
                       5.35940E-03,5.35940E-03,5.53401E-03,5.71430E-03,5.71430E-03,
                       6.00000E-03,8.00000E-03,1.00000E-02,1.50000E-02,2.00000E-02,
                       3.00000E-02,3.59846E-02,3.59846E-02,4.00000E-02,5.00000E-02,
                       6.00000E-02,8.00000E-02,1.00000E-01,1.50000E-01,2.00000E-01,
                       3.00000E-01,4.00000E-01,5.00000E-01,6.00000E-01,8.00000E-01,
                       1.00000E+00])

# Mu/Rho associés aux énergies pour le Cs pour l'axe des y (ordonnées) (cm2/g)
mu_rho_Cs = np.array([9.365E+03,8.775E+03,8.214E+03,8.685E+03,7.576E+03,6.584E+03,
                      6.888E+03,4.335E+03,2.226E+03,8.319E+02,4.055E+02,2.303E+02,
                      2.290E+02,6.674E+02,6.184E+02,5.645E+02,7.692E+02,7.146E+02,
                      6.556E+02,7.547E+02,6.711E+02,3.214E+02,1.793E+02,6.104E+01,
                      2.822E+01,9.507E+00,5.863E+00,3.143E+01,2.381E+01,1.340E+01,
                      8.248E+00,3.836E+00,2.124E+00,7.589E-01,3.941E-01,1.863E-01,
                      1.257E-01,9.912E-02,8.431E-02,6.789E-02,5.854E-02])

#Energies pour l'axe des x (abscisse) de l'Y (MeV)
energie_Y = np.array([1.00000E-03,1.50000E-03,2.00000E-03,2.08000E-03,2.08000E-03,
                      2.11741E-03,2.15550E-03,2.15550E-03,2.26140E-03,2.37250E-03,
                      2.37250E-03,3.00000E-03,4.00000E-03,5.00000E-03,6.00000E-03,
                      1.00000E-02,1.50000E-02,1.70384E-02,1.70384E-02,2.00000E-02,
                      3.00000E-02,4.00000E-02,5.00000E-02,6.00000E-02,8.00000E-02,
                      1.00000E-01,1.50000E-01,2.00000E-01,3.00000E-01,4.00000E-01,
                      5.00000E-01,6.00000E-01,8.00000E-01,1.00000E+00])

# Mu/Rho associés aux énergies pour l'Y pour l'axe des y (ordonnées) (cm2/g)
mu_rho_Y = np.array([3.864E+03,1.493E+03,7.422E+02,6.738E+02,2.627E+03,2.466E+03,
                     2.342E+03,3.264E+03,2.916E+03,2.597E+03,2.962E+03,1.654E+03,
                     7.936E+02,4.424E+02,2.725E+02,1.258E+02,6.871E+01,2.279E+01,
                     1.612E+01,1.029E+02,6.855E+01,2.330E+01,1.065E+01,5.764E+00,
                     3.493E+00,1.607E+00,9.047E-01,3.595E-01,2.149E-01,1.289E-01,
                     1.006E-01,8.613E-02,7.703E-02,6.546E-02,5.795E-02])


# DONNÉES INTERPOLATION (Photons) POUR BLOC B

#Energies pour l'axe des x (abscisse) de l'Y (MeV)
energie_Y_sigma = np.array([1.0000E-03,1.0715E-03,1.1482E-03,1.2023E-03,1.2589E-03,
                            1.3183E-03,1.3804E-03,1.4454E-03,1.5136E-03,1.5849E-03,
                            1.6596E-03,1.7378E-03,1.8197E-03,1.9055E-03,1.9498E-03,
                            1.9953E-03,2.0815E-03,2.0815E-03,2.0893E-03,2.1380E-03,
                            2.1597E-03,2.1597E-03,2.1878E-03,2.2909E-03,2.3549E-03,
                            2.3549E-03,2.4547E-03,2.5704E-03,2.6915E-03,2.8184E-03,
                            2.9512E-03,3.0903E-03,3.2359E-03,3.3884E-03,3.5481E-03,
                            3.7154E-03,3.8905E-03,4.0738E-03,4.2658E-03,4.4668E-03,
                            4.6774E-03,4.8978E-03,5.1286E-03,5.3703E-03,5.6234E-03,
                            5.8884E-03,6.1660E-03,6.4565E-03,6.7608E-03,7.0795E-03,
                            7.4131E-03,7.7625E-03,8.1283E-03,8.5114E-03,8.9125E-03,
                            9.3325E-03,9.7724E-03,1.0000E-02,1.0471E-02,1.0965E-02,
                            1.1482E-02,1.2023E-02,1.2589E-02,1.3183E-02,1.3804E-02,
                            1.4454E-02,1.5136E-02,1.5849E-02,1.6596E-02,1.7000E-02,
                            1.7000E-02,1.7783E-02,1.8621E-02,1.9498E-02,2.0417E-02,
                            2.1380E-02,2.2387E-02,2.3442E-02,2.4547E-02,2.5704E-02,
                            2.6915E-02,2.8184E-02,2.9512E-02,3.0903E-02,3.2359E-02,
                            3.3884E-02,3.5481E-02,3.7154E-02,3.8905E-02,4.0738E-02,
                            4.2658E-02,4.4668E-02,4.6774E-02,4.8978E-02,5.1286E-02,
                            5.3703E-02,5.6234E-02,5.8884E-02,6.1660E-02,6.4565E-02,
                            6.7608E-02,7.0795E-02,7.4131E-02,7.7625E-02,8.1283E-02,
                            8.5114E-02,8.9125E-02,9.3325E-02,9.7724E-02,1.0000E-01,
                            1.0471E-01,1.0965E-01,1.1482E-01,1.2023E-01,1.2589E-01,
                            1.3183E-01,1.3804E-01,1.4454E-01,1.5136E-01,1.5849E-01,
                            1.6596E-01,1.7378E-01,1.8197E-01,1.9055E-01,1.9953E-01])

#Energie pour l'axe x (abscisse) du CS (Mev)
energie_CS_sigma = np.array([1.0000E-03,1.0595E-03,1.0595E-03,1.1220E-03,1.1964E-03,
                             1.1964E-03,1.2589E-03,1.3490E-03,1.4454E-03,1.5488E-03,
                             1.6218E-03,1.7378E-03,1.8197E-03,1.9055E-03,1.9953E-03,
                             2.0893E-03,2.1878E-03,2.2909E-03,2.3988E-03,2.5119E-03,
                             2.6303E-03,2.7542E-03,2.8840E-03,3.0199E-03,3.1623E-03,
                             3.3113E-03,3.4674E-03,3.6308E-03,3.8019E-03,3.9811E-03,
                             4.1687E-03,4.3652E-03,4.5709E-03,4.7863E-03,4.8978E-03,
                             5.0061E-03,5.0061E-03,5.0119E-03,5.2481E-03,5.3632E-03,
                             5.3632E-03,5.4954E-03,5.6849E-03,5.6849E-03,5.8884E-03,
                             6.1660E-03,6.4565E-03,6.7608E-03,7.0795E-03,7.4131E-03,
                             7.7625E-03,8.1283E-03,8.5114E-03,8.9125E-03,9.3325E-03,
                             9.7724E-03,1.0000E-02,1.0471E-02,1.0965E-02,1.1482E-02,
                             1.2023E-02,1.2589E-02,1.3183E-02,1.3804E-02,1.4454E-02,
                             1.5136E-02,1.5849E-02,1.6596E-02,1.7378E-02,1.8197E-02,
                             1.9055E-02,1.9953E-02,2.0893E-02,2.1878E-02,2.2909E-02,
                             2.3988E-02,2.5119E-02,2.6303E-02,2.7542E-02,2.8840E-02,
                             3.0200E-02,3.1623E-02,3.3113E-02,3.4674E-02,3.5985E-02,
                             3.5985E-02,3.7154E-02,3.8905E-02,4.0738E-02,4.2658E-02,
                             4.4668E-02,4.6774E-02,4.8978E-02,5.1286E-02,5.3703E-02,
                             5.6234E-02,5.8884E-02,6.1660E-02,6.4565E-02,6.7608E-02,
                             7.0795E-02,7.4131E-02,7.7625E-02,8.1283E-02,8.5114E-02,
                             8.9125E-02,9.3325E-02,9.7724E-02,1.0000E-01,1.0471E-01,
                             1.0965E-01,1.1482E-01,1.2023E-01,1.2589E-01,1.3183E-01,
                             1.3804E-01,1.4454E-01,1.5136E-01,1.5849E-01,1.6596E-01,
                             1.7378E-01,1.8197E-01,1.9055E-01,1.9953E-01])




# Section efficace de Thomson-Rayleigh associés aux énergies pour l'Y pour l'axe des y (ordonnées)
sigma_TR = np.array([6.8494E+02,6.7142E+02,6.5552E+02,6.4419E+02,6.3191E+02,6.1798E+02,
                     6.0248E+02,5.8570E+02,5.6728E+02,5.4634E+02,5.2218E+02,4.9413E+02,
                     4.5925E+02,4.1233E+02,3.8093E+02,3.3812E+02,2.5811E+02,2.5811E+02,
                     2.6571E+02,3.3748E+02,3.7643E+02,3.7643E+02,4.2457E+02,5.1725E+02,
                     5.4396E+02,5.4396E+02,6.2590E+02,6.6313E+02,6.8367E+02,6.9407E+02,
                     6.9805E+02,6.9798E+02,6.9330E+02,6.8602E+02,6.7587E+02,6.6477E+02,
                     6.5159E+02,6.3667E+02,6.2126E+02,6.0488E+02,5.8781E+02,5.7020E+02,
                     5.5253E+02,5.3432E+02,5.1606E+02,1.9801E+02,4.7946E+02,4.6159E+02,
                     4.4337E+02,1.2563E+02,4.0782E+02,3.9035E+02,3.7316E+02,3.5621E+02,
                     3.3925E+02,3.2260E+02,3.0631E+02,2.9820E+02,2.8215E+02,2.6641E+02,
                     2.5108E+02,2.3578E+02,2.2106E+02,2.0630E+02,1.9200E+02,1.7765E+02,
                     1.6282E+02,1.4681E+02,1.2338E+02,1.0828E+02,1.0828E+02,1.2895E+02,
                     1.3075E+02,1.2797E+02,1.2332E+02,1.1806E+02,1.1247E+02,1.0664E+02,
                     1.0084E+02,9.5180E+01,8.9601E+01,8.4271E+01,7.9030E+01,7.4089E+01,
                     6.9336E+01,6.4834E+01,6.0530E+01,5.6454E+01,5.2487E+01,4.8797E+01,
                     4.5236E+01,4.1923E+01,3.8853E+01,3.6008E+01,3.3318E+01,3.0816E+01,
                     2.8472E+01,2.6270E+01,2.4238E+01,2.2363E+01,2.0611E+01,1.8995E+01,
                     1.7505E+01,1.6132E+01,1.4866E+01,1.3700E+01,1.2626E+01,1.1630E+01,
                     1.0705E+01,1.0270E+01,9.4531E+00,8.7010E+00,8.0057E+00,7.3561E+00,
                     6.7591E+00,6.2106E+00,5.7035E+00,5.2322E+00,4.7998E+00,4.4032E+00,
                     4.0393E+00,3.7021E+00,3.3912E+00,3.1063E+00,2.8454E+00])

#Section efficace de Thomson-Rayleigh associés aux energies pour le CS pour l'axe des y (ordonnées)
sigma_TR_Cs = np.array([1.2643E+03,1.3247E+03,1.3247E+03,1.4117E+03,1.4492E+03,1.4492E+03,
                        1.5234E+03,1.5589E+03,1.5692E+03,1.5691E+03,1.5647E+03,1.5511E+03,
                        1.5357E+03,1.5179E+03,1.4970E+03,1.4753E+03,1.4498E+03,1.4248E+03,
                        1.3955E+03,1.3647E+03,1.3339E+03,1.2994E+03,1.2653E+03,1.2284E+03,
                        1.1901E+03,1.1513E+03,1.1103E+03,1.0675E+03,1.0227E+03,9.7495E+02,
                        9.2365E+02,8.6605E+02,7.9772E+02,7.0148E+02,6.1554E+02,5.4876E+02,
                        5.4876E+02,5.5074E+02,6.6371E+02,6.6808E+02,6.6808E+02,7.3709E+02,
                        7.7041E+02,7.7041E+02,8.4008E+02,8.6833E+02,8.7362E+02,8.6740E+02,
                        8.5355E+02,8.3408E+02,8.1108E+02,7.8527E+02,7.5770E+02,7.2915E+02,
                        7.0060E+02,6.7074E+02,6.5629E+02,6.2734E+02,5.9841E+02,5.7059E+02,
                        5.4271E+02,5.1619E+02,4.9048E+02,4.6532E+02,4.4146E+02,4.1773E+02,
                        3.9526E+02,3.7359E+02,3.5245E+02,3.3202E+02,3.1231E+02,2.9314E+02,
                        2.7490E+02,2.5696E+02,2.3997E+02,2.2354E+02,2.0781E+02,1.9284E+02,
                        1.7838E+02,1.6469E+02,1.5147E+02,1.3850E+02,1.2535E+02,1.0983E+02,
                        9.1917E+01,9.1917E+01,1.0256E+02,1.0420E+02,1.0111E+02,9.6609E+01,
                        9.1550E+01,8.6384E+01,8.1240E+01,7.6163E+01,7.1206E+01,6.6464E+01,
                        6.1831E+01,5.7496E+01,5.3301E+01,4.9413E+01,4.5720E+01,4.2253E+01,
                        3.9049E+01,3.6015E+01,3.3202E+01,3.0609E+01,2.8218E+01,2.6014E+01,
                        2.4977E+01,2.2992E+01,2.1165E+01,1.9483E+01,1.7924E+01,1.6470E+01,
                        1.5134E+01,1.3906E+01,1.2778E+01,1.1742E+01,1.0784E+01,9.8978E+00,
                        9.0846E+00,8.3382E+00,7.6531E+00,7.0226E+00])



# Section efficace de Photoélectrique associés aux énergies pour l'Y pour l'axe des y (ordonnées)
sigma_P = np.array([5.6924E+05,4.8575E+05,4.1376E+05,3.7155E+05,3.3333E+05,2.9890E+05,
                    2.6793E+05,2.3992E+05,2.1481E+05,1.9214E+05,1.7191E+05,1.5356E+05,
                    1.3721E+05,1.2252E+05,1.1572E+05,1.0931E+05,9.8454E+04,3.7305E+05,
                    3.7014E+05,3.5271E+05,3.4441E+05,4.7682E+05,4.6327E+05,4.1547E+05,
                    3.8781E+05,4.4392E+05,4.0145E+05,3.5830E+05,3.1933E+05,2.8455E+05,
                    2.5337E+05,2.2564E+05,2.0088E+05,1.7863E+05,1.5885E+05,1.4107E+05,
                    1.2519E+05,1.1108E+05,9.8514E+04,8.7240E+04,7.7250E+04,6.8389E+04,
                    6.0504E+04,5.3523E+04,4.7307E+04,4.1778E+04,3.6907E+04,3.2595E+04,
                    2.8762E+04,2.5377E+04,2.2380E+04,1.9729E+04,1.7394E+04,1.5324E+04,
                    1.3495E+04,1.1884E+04,1.0464E+04,9.8152E+03,8.6368E+03,7.5993E+03,
                    6.6830E+03,5.8755E+03,5.1653E+03,4.5382E+03,3.9876E+03,3.5039E+03,
                    3.0758E+03,2.7007E+03,2.3710E+03,2.2147E+03,1.5190E+04,1.3520E+04,
                    1.2008E+04,1.0635E+04,9.4349E+03,8.3700E+03,7.3978E+03,6.5384E+03,
                    5.7783E+03,5.1067E+03,4.5103E+03,3.9752E+03,3.5034E+03,3.0878E+03,
                    2.7213E+03,2.3952E+03,2.1056E+03,1.8511E+03,1.6271E+03,1.4302E+03,
                    1.2559E+03,1.1016E+03,9.6615E+02,8.4737E+02,7.4320E+02,6.5095E+02,
                    5.6988E+02,4.9890E+02,4.3678E+02,3.8223E+02,3.3410E+02,2.9204E+02,
                    2.5527E+02,2.2313E+02,1.9497E+02,1.7019E+02,1.4857E+02,1.2970E+02,
                    1.1322E+02,1.0577E+02,9.2329E+01,8.0553E+01,7.0270E+01,6.1300E+01,
                    5.3476E+01,4.6649E+01,4.0695E+01,3.5501E+01,3.0971E+01,2.7019E+01,
                    2.3572E+01,2.0565E+01,1.7942E+01,1.5663E+01,1.3684E+01])

# Section efficace de Compton associés aux énergies pour l'Y pour l'axe des y (ordonnées)
sigma_C = np.array([1.2411E+00,1.3524E+00,1.4737E+00,1.5605E+00,1.6524E+00,1.7386E+00,
                    1.8293E+00,1.9247E+00,2.0251E+00,2.1307E+00,2.2336E+00,2.3415E+00,
                    2.4547E+00,2.5732E+00,2.6347E+00,2.6976E+00,2.8120E+00,2.8120E+00,
                    2.8224E+00,2.8869E+00,2.9157E+00,2.9157E+00,2.9529E+00,3.0896E+00,
                    3.1744E+00,3.1744E+00,3.3065E+00,3.4565E+00,3.6102E+00,3.7708E+00,
                    3.9384E+00,4.1136E+00,4.2917E+00,4.4725E+00,4.6609E+00,4.8572E+00,
                    5.0618E+00,5.2692E+00,5.4792E+00,5.6976E+00,5.9247E+00,6.1608E+00,
                    6.3966E+00,6.6314E+00,6.8748E+00,7.1272E+00,7.3888E+00,7.6450E+00,
                    7.8946E+00,8.1523E+00,8.4185E+00,8.6933E+00,8.9616E+00,9.2221E+00,
                    9.4902E+00,9.7661E+00,1.0050E+01,1.0195E+01,1.0464E+01,1.0739E+01,
                    1.1022E+01,1.1312E+01,1.1610E+01,1.1884E+01,1.2164E+01,1.2450E+01,
                    1.2744E+01,1.3044E+01,1.3310E+01,1.3451E+01,1.3451E+01,1.3719E+01,
                    1.3999E+01,1.4284E+01,1.4548E+01,1.4789E+01,1.5034E+01,1.5283E+01,
                    1.5537E+01,1.5760E+01,1.5953E+01,1.6147E+01,1.6345E+01,1.6544E+01,
                    1.6725E+01,1.6887E+01,1.7050E+01,1.7215E+01,1.7381E+01,1.7512E+01,
                    1.7607E+01,1.7702E+01,1.7798E+01,1.7895E+01,1.7959E+01,1.7991E+01,
                    1.8024E+01,1.8056E+01,1.8089E+01,1.8092E+01,1.8067E+01,1.8041E+01,
                    1.8016E+01,1.7991E+01,1.7939E+01,1.7863E+01,1.7786E+01,1.7710E+01,
                    1.7634E+01,1.7596E+01,1.7475E+01,1.7354E+01,1.7235E+01,1.7116E+01,
                    1.6998E+01,1.6839E+01,1.6682E+01,1.6527E+01,1.6373E+01,1.6220E+01,
                    1.6034E+01,1.5850E+01,1.5668E+01,1.5488E+01,1.5310E+01])

# Données des couches électroniques de l'yttrium
# Format : Couche, N (nombre d'électrons), B (énergie de liaison en MeV), U (énergie cinétique en MeV)

couche_elec = {
    "K": {"N": 2.0, "B": 0.017000, "U": 0.021532},
    "L1": {"N": 2.0, "B": 0.002355, "U": 0.004415},
    "L2": {"N": 2.0, "B": 0.002160, "U": 0.004413},
    "L3": {"N": 4.0, "B": 0.002082, "U": 0.004127},
    "M1": {"N": 2.0, "B": 0.000386, "U": 0.001131},
    "M2": {"N": 2.0, "B": 0.000312, "U": 0.001075},
    "M3": {"N": 4.0, "B": 0.000300, "U": 0.001017},
    "M4": {"N": 4.0, "B": 0.000169, "U": 0.000901},
    "M5": {"N": 6.0, "B": 0.000167, "U": 0.000887},
    "N1": {"N": 2.0, "B": 0.000053, "U": 0.000233},
    "N2": {"N": 2.0, "B": 0.000034, "U": 0.000190},
    "N3": {"N": 4.0, "B": 0.000032, "U": 0.000180},
    "N4": {"N": 0.4, "B": 0.000005, "U": 0.000078},
    "N5": {"N": 0.6, "B": 0.000005, "U": 0.000076},
    "O1": {"N": 2.0, "B": 0.000006, "U": 0.000027},
}

# ------------------------------
# Function Definitions
# ------------------------------


def mu_mass_Y_Pho(E):
       f = interp1d(energie_Y, mu_rho_Y, kind="linear", fill_value="extrapolate")
       mu = f(E)  # Interpolate with interp1d
       print(f'BLOC D : Le mu correspondant à cette Energie par interpollation et le suivant : {mu:.6f}')
       return mu

def mu_mass_Cs_Pho(E):
       f = interp1d(energie_Cs, mu_rho_Cs, kind="linear", fill_value="extrapolate")
       mu = f(E)  # Interpolate with interp1d
       print(f'BLOC D : Le mu correspondant à cette Energie par interpollation et le suivant : {mu:.6f}')
       return mu


def mu_mass_Pho(E, Z):  # ATTENTION EXPRIMÉE EN cm2.g-1 !!!!!!!!!

    if Z == 39:  # Le Materiaux est de l'Yttrium
        print("BLOC D : Le materiaux choisi est de l'Yttrium")
        mu = mu_mass_Y_Pho(E)
    elif Z == 55:  # Le Materiaux est du Cesium
        print("BLOC D : Le materiaux choisi est du Cesium")
        mu = mu_mass_Cs_Pho(E)
    else:
        print("BLOC D : Le materiaux choisi est ni de l'Yttrium ni du Cesium")

    return mu


def Energie_initiale():
    C = np.random.uniform(0, 1)
    if (C < P_pho_10):
        return E_pho_10
    elif (C < P_pho_30 + P_pho_10 and C >= P_pho_10):
        return E_pho_30
    elif (C < (P_pho_50 + P_pho_30 + P_pho_10) and C >= (P_pho_10 + P_pho_30)):
        return E_pho_50
    else:
        return E_pho_100


def Position_initiale():  # J'ai fait une fonction mais pas sûr que ca soit bien utile

    # Choix d'un Rayons aléatoire entre R1 et R2
    R = np.random.uniform(R_min, R_max)  # R_min = R1 et R_max = R2
    # Choix d'un angle aléatoire entre 0 et 2pi pour faire le tour de la couronne
    phi = np.random.uniform(0, 2 * np.pi)
    x = R * np.cos(phi)
    y = R * np.sin(phi)

    return x, y

def density(Z):
       if Z == 39:  # Yttrium
           return 4.472  # g/cm^3 (NIST value)
       elif Z == 55:  # Cesium
           return 1.93  # g/cm^3 (NIST value)
       else:
           return 1 # Default value, but consider raising an exception

def generate_point(R_min, R_max):
    # Générer un rayon aléatoire entre les rayons entrés
    r = np.sqrt(np.random.uniform(R_min ** 2, R_max ** 2))
    # Générer un angle aléatoire entre 0 et 2*pi
    theta = np.random.uniform(0, 2 * np.pi)

    # Convertir en coordonnées cartésiennes
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y

def libre_parcours_moyen(Z, E):
    r = np.random.uniform(0, 1)  # variable aléatoire r uniformément distribuée entre 0 et 1
    LPM = -np.log(r) /(mu_mass_Pho(E, Z) * density(Z))  # Calcul LPM en utilisant la densité et la section efficace massique
    return LPM


# Coordonnées d'émission dans une couronne
def Position_interaction(E, Z, x_p, y_p):  # Add parameters
       LPM = libre_parcours_moyen(Z, E)
       phi = np.random.uniform(-np.pi/2, np.pi/2)
       x = LPM * np.cos(phi) + x_p
       y = LPM * np.sin(phi) + y_p
       return x, y, LPM, phi  # Return LPM


def Position_interaction_suivante(E, Z, phi_premiere_interaction, x_p, y_p):
    # position suivante de la particule
    LPM = libre_parcours_moyen(E, Z)
    phi = phi_premiere_interaction + np.random.uniform(0, 2 * np.pi) - phi_premiere_interaction  # Génére un nouvel angle basé sur l'angle précédent
    x = LPM * np.cos(phi) + x_p
    y = LPM * np.sin(phi) + y_p
    return x, y, LPM, phi


#---------------------------
#    THOMSON
#---------------------------
r0 = 2.818e-15  # Rayon de l'électron

def thomson(theta):
    section_eff_thomson = 0.5 * r0**2 * (1 + np.cos(theta)**2)
    return section_eff_thomson

#---------------------------
#    PHOTOÉLECTRIQUE
#---------------------------
def photoelectric(Z, E):
    n = 4.5
    m = 3.5
    section_eff_photo = (Z ** n) * (E ** -m) # Relation de proportionnalité à vérifier
    return section_eff_photo

#---------------------------
#    KLEIN NISHINA
#---------------------------
m_e_c2 = 511e3  # Énergie au repos de l'électron en keV

def klein_nishina(E0, theta):
    E_prime = E0 / (1 + (E0 / m_e_c2) * (1 - np.cos(theta)))
    section_eff_compton = 0.5 * r0**2 * (E_prime / E0)**2 * (E_prime / E0 + E0 / E_prime - np.sin(theta)**2)
    return section_eff_compton

# -----------------------------
#  DEFINITION TYPE INTERACTION
# -----------------------------

def type_interaction(Z, E, theta):
    # Calcul des probabilités d'interaction normalisées directement
    Sigma_tot = thomson(theta) + photoelectric(Z, E) + klein_nishina(E, theta)
    Proba_Thomson = thomson(theta) / Sigma_tot
    Proba_Photoelec = photoelectric(Z, E) / Sigma_tot
    Proba_Compton = klein_nishina(E, theta) / Sigma_tot

    # Tirage aléatoire pour déterminer l'interaction
    R = np.random.uniform(0, 1)
    if R <= Proba_Thomson:
        return 'TR'  # Interaction Thomson
    elif R <= Proba_Thomson + Proba_Photoelec:
        return 'P'  # Interaction photoélectrique
    else:
        return 'C'  # Interaction Compton

# ---------------------------
#  DEFINITION INTERACTION
# ---------------------------
def interaction(Z, E, theta):
    interaction_type = type_interaction(Z, E, theta)
    return interaction_type

# -----------------------------
#  Fonction pour tirer une couche électronique pour un effet photoélectrique
# -----------------------------
def tirage_couche_PE():
    """
    Réalise un tirage aléatoire de la couche électronique dans un effet photoélectrique (PE).
    Returns: txt: La couche électronique sélectionnée ("K", "L1", "L2", "L3").
    """
    # Définir les couches principales et leurs probabilités
    couches_principales = ['K', 'L']
    probabilites_principales = [0.5, 0.5]  # Probabilité pour K et L
    couche_principale = np.random.choice(couches_principales, p=probabilites_principales)

    if couche_principale == "K":
        return "K"
    else:
        # Tirer entre L1, L2, et L3 avec probabilités pondérées
        sous_couches = ['L1', 'L2', 'L3']
        nombre_electrons = [2, 2, 4]  # Nombre d'électrons pour L1, L2, et L3
        total_electrons = sum(nombre_electrons)
        probabilites_sous_couches = [n / total_electrons for n in nombre_electrons]
        sous_couche = np.random.choice(sous_couches, p=probabilites_sous_couches)
        return sous_couche

# -----------------------------
#  Calcul de l'énergie restante après l'interaction
# -----------------------------
def energie_restante(interaction_type):
    """
    Calcule l'énergie restante après l'interaction, en soustrayant l'énergie de liaison de la sous-couche.
    Args:
        interaction_type (str): Le type d'interaction (PE avec couche spécifique).
    Returns:
        float: L'énergie restante après interaction.
    """
    # Sélectionner une énergie de photon initiale
    photon_energy = select_photon_energy()  # Assurez-vous que select_photon_energy est défini

    # Tirage pour la couche si interaction photoélectrique
    if interaction_type == 'P':
        couche = tirage_couche_PE()

        # Récupérer l'énergie de liaison de la couche via le dictionnaire
        energie_liaison = couche_elec[couche]["B"]

        # Calcul de l'énergie restante après soustraction de l'énergie de liaison
        energie_restante = photon_energy - energie_liaison

        # Retourner l'énergie restante
        return energie_restante, couche
    else:
        return photon_energy, None  # Pour les autres types d'interaction
def rotation_plan(phi_gen, phi_precedant):
    phi = phi_gen - phi_precedant
    return phi


def Apres_interaction(Z, E, phi_precedant):
    if type_interaction(Z, E, phi_precedant) == 'TR':
        LPM = 1  # CETTE VALEUR EST A DÉFINIR
        phi = 1  # CETTE VALEUR EST A DÉFINIR
        E = E  # pas de perte d'énergie

    elif type_interaction(Z, E, phi_precedant) == 'P':
        LPM = 2  # CETTE VALEUR EST A DÉFINIR
        phi = 2  # CETTE VALEUR EST A DÉFINIR
        E = 0  # E - E_photoelec # CETTE VALEUR EST A DÉFINIR
        # Pour cette partie on va surment devoir determiner l'énergie de liaison
        # de l'éléctron à l'atome et tirer aléatoirement la couche sur laquelle se trouve l'éléctron

    elif type_interaction(Z, E, phi_precedant) == 'C':
        phi = np.random.uniform(-np.pi, np.pi)
        E2 = E / (1 + (E / m_e_c2) * (1 - np.cos(phi)))  # E_prime Energie du photons diffusé après interaction Compton
        LPM = libre_parcours_moyen(E2)
        phi = phi_precedant
        E = E2

    else:
        print(f'BLOC B : Ce type d interaction n existe pas ! Votre interaction est : {type_interaction} ')

        # Valeurs choisies par défaut pour couper la simulation E < E_de_coupure
        LPM = 0
        phi = 0
        E = 0

    return LPM, phi, E


def visualiser_photons_et_trajets(R1, R2, n_photons, longueur_trajet=2.0):
    """
    Visualise une couronne circulaire, les photons qui en partent, et leurs trajectoires.

    Args:
        R1 (float): Rayon interne de la couronne (en cm).
        R2 (float): Rayon externe de la couronne (en cm).
        n_photons (int): Nombre de photons à émettre.
        longueur_trajet (float): Longueur des trajectoires des photons (en cm).

    Returns:
        None: Affiche la visualisation.
    """
    # Générer les coordonnées polaires pour les photons émis dans la couronne
    angles = np.random.uniform(0, 2 * np.pi, n_photons)  # Angles aléatoires
    rayons = np.random.uniform(R1, R2,n_photons)  # Rayons aléatoires dans la couronne

    # Convertir les coordonnées polaires en coordonnées cartésiennes pour les photons
    x_photons = rayons * np.cos(angles)
    y_photons = rayons * np.sin(angles)

    # Calculer les directions de sortie des photons
    angles_trajets = np.random.uniform(0, 2 * np.pi,n_photons)  # Directions aléatoires
    x_trajets = np.cos(angles_trajets)
    y_trajets = np.sin(angles_trajets)

    # Calculer les coordonnées de fin des trajectoires
    x_end = x_photons + longueur_trajet * x_trajets
    y_end = y_photons + longueur_trajet * y_trajets

    # Visualisation de la couronne, des photons et de leurs trajectoires
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')  # Assurer une échelle égale sur les axes x et y

    # Tracer la couronne (zone entre R1 et R2)
    cercle_interne = plt.Circle((0, 0), R1, color='blue', alpha=0.2)
    cercle_externe = plt.Circle((0, 0), R2, color='blue', alpha=0.2)
    ax.add_artist(cercle_externe)
    ax.add_artist(cercle_interne)

    # Tracer les photons (points dans la couronne)
    ax.scatter(x_photons, y_photons, color='red', s=10, alpha=0.7)

    # Tracer les trajectoires des photons (lignes)
    for i in range(n_photons): ax.plot([x_photons[i], x_end[i]], [y_photons[i], y_end[i]],color='green', alpha=0.5)

    # Définir les limites de l'affichage
    ax.set_xlim(-R2 - 1, R2 + 1)
    ax.set_ylim(-R2 - 1, R2 + 1)
    ax.set_title(
        "Visualisation de la Couronne, des Photons et de leurs Trajets")

    # Afficher le graphique
    plt.show()


# ------------------------------
# Main Simulation Logic
# ------------------------------
if __name__ == "__main__":
    N = 100

    # initilaisation des vecteurs
    E = np.zeros((N, 100))
    x = np.zeros((N, 100))
    y = np.zeros((N, 100))

    # Boucle sur le nombre de particules
    for i in range(N):
        j = 0
        # Energie initiale de la source
        E[i][j] = Energie_initiale()
        # Position initiale de la particule
        x[i][j], y[i][j] = Position_initiale()
        # Position de l'interaction
        #x[i][j + 1], y[i][j + 1], A, B = Position_interaction(N)

        # objectif : faire que EV, ZV, x_pV et y_pV dépendent de N

        # Variables dépendantes de N
        EV = E[i][j] * N
        ZV = Z * N
        x_pV = x[i][j]
        y_pV = y[i][j]

        x[i][j + 1], y[i][j + 1] = Position_interaction(EV, ZV, x_pV, y_pV)

        while (E[i][j] > Energie_coupure() and j < 99):
            # Recalculer les variables dépendantes de Z
            EV = E[i][j] * N
            ZV = Z * N
            x_pV = x[i][j]
            y_pV = y[i][j]

            # Energie, phi et LPM après interaction
            E[i][j + 1] = E[i][j] - 1  # - Energie_perdue
            x[i][j + 1], y[i][j + 1] = Position_interaction(EV, ZV, x_pV, y_pV)
            j = j + 1

# def Position_interaction(E, Z, x_p, y_p)

# ------------------------------
# Visualization
# ------------------------------
visualiser_photons_et_trajets(R_min, R_max, N)  # Call visualization function