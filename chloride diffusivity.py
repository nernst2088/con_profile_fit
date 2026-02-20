#calculate chloride diffusivity in concrete using Fick's 2nd law and concentration profile
#2nd Fick's law is as following:
#D = 2*k*L/V
#D is diffusivity
#k is the first-order rate constant
#L is the length of the sample
#V is the volume of the sample
#Concentration profile is as following:
#txt file contains 2 columns of data:
#1st column is the distance from the left side of the sample in mm
#2nd column is the concentration of the sample in mg/L or %
#time in days is in the 1st line of the txt file, followed by the number
#there is blank line after the time data
#then the column name
#then the depth-concentration data
#the following python script will calculate the diffusivity of chloride in concrete
#the script will also plot the concentration profile and the diffusivity
import numpy as np
import matplotlib.pyplot as plt

# read data from txt file
data = np.loadtxt('chloride_concentration.txt')
time = data["",1]
depth = data[:,0]
concentration = data[:,1]

# calculate diffusivity using Fick's 2nd law
L = 0.05 # length of the sample in m
V = 0.001 # volume of the sample in m^3
k = 0.1 # first-order rate constant in 1/s
D = 2*k*L/V # diffusivity in m^2/s
diffusivity = D*1e6 # convert to um^2/s

# plot concentration profile and diffusivity
plt.plot(depth, concentration)
plt.xlabel('Depth (mm)')
plt.ylabel('Concentration (mg/L)')
plt.title('Concentration Profile and Diffusivity')
plt.text(0.025, 0.5, f'Diffusivity: {diffusivity:.2f} um^2/s')
plt.show()

print(f'Diffusivity: {diffusivity:.2f} um^2/s')

# calculate the slope of the concentration profile
slope = np.gradient(concentration, depth)

# plot the slope of the concentration profile

    plt.plot(depth, slope)
    plt.xlabel('Depth (mm)')
    plt.ylabel('Slope of Concentration Profile')
    plt.title('Slope of Concentration Profile')
    plt.show()

        print(f'Slope of Concentration Profile: {slope[-1]:.2f} mg/L/mm')

# calculate the rate constant from the slope of the concentration profile
rate_constant = -slope[-1]/concentration[-1]

print(f'Rate Constant: {rate_constant:.2f} 1/s')

# calculate the time required for the chloride concentration to reach 50% of the initial concentration
time_to_50 = (0.5 - concentration[0]) / rate_constant

print(f'Time to Reach 50% Concentration: {time_to_50:.2f} days')

# calculate the time required for the chloride concentration to reach 90% of the initial concentration
time_to_90 = (0.9 - concentration[0]) / rate_constant

print(f'Time to Reach 90% Concentration: {time_to_90:.2f} days')

# calculate the time required for the chloride concentration to reach 99% of the initial concentration
time_to_99 = (0.99 - concentration[0]) / rate_constant  

print(f'Time to Reach 99% Concentration: {time_to_99:.2f} days')    

# calculate the time required for the chloride concentration to reach 99.9% of the initial concentration
time_to_999 = (0.999 - concentration[0]) / rate_constant

print(f'Time to Reach 99.9% Concentration: {time_to_999:.2f} days')

# calculate the time required for the chloride concentration to reach 99.99% of the initial concentration
time_to_9999 = (0.9999 - concentration[0]) / rate_constant

print(f'Time to Reach 99.99% Concentration: {time_to_9999:.2f} days')

# calculate the time required for the chloride concentration to reach 99.999% of the initial concentration
time_to_99999 = (0.99999 - concentration[0]) / rate_constant

print(f'Time to Reach 99.999% Concentration: {time_to_99999:.2f} days')

# calculate the time required for the chloride concentration to reach 99.9999% of the initial concentration
time_to_999999 = (0.999999 - concentration[0]) / rate_constant
