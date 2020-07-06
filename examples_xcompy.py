import numpy as np
import xcompy as xc
import matplotlib.pyplot as plt

# plot the attenuation values for the elemnt Oxygen
element = 'Au'
energies = np.logspace(1,3,101)  # define energies in keV
attens = xc.mixatten(element,energies)
rho = 19.3 #Density of gold [g/cm^3]

element = 'Au'
attens = xc.mixatten(element,energies)
plt.loglog(energies,attens*rho)
element = 'Ca'
attens = xc.mixatten(element,energies)
plt.loglog(energies,attens)
plt.xlabel('Energy (keV)')
plt.ylabel('Attenuation (g/cm^2)')
plt.title('Mass Attenuation for the element: ' + element)


#plot the attenuation values for a compound
compound = 'O2'
energies = np.logspace(0,5,101)  # define energies in keV
attens = xc.mixatten(compound,energies)

plt.loglog(energies,attens)
plt.xlabel('Energy (keV)')
plt.ylabel('Attenuation (g/cm^2)')
plt.title('Mass Attenuation for the compound: ' + compound)


# plot the attenuation values for a mixture of water and sodium 95% and 5% by mass    
mixture = 'H2O(95)Na(5)'
energies = np.logspace(0,5,101)  # define energies in keV
attens = xc.mixatten(mixture,energies)

plt.loglog(energies,attens)
plt.xlabel('Energy (keV)')
plt.ylabel('Attenuation (g/cm^2)')
plt.title('Mass Attenuation for the mixture: ' + mixture)




#Split Test
elem = 5
rootpath = '/Users/vargasp/Research/Libraries/Python_Lib/XCOMPy'

    
f = open(rootpath +'/data/MDATX3.' + str(elem).zfill(3))
t1 = f.read().split()

f = open(rootpath +'/data/MDATX3.' + str(elem).zfill(3))
t2 = f.read().split(' \n')

    
    
    
