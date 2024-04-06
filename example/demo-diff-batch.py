import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import erf

# Fick's second law function definition with time_value included in the parameters array
def fick_second_law(z, *params):
    D, C0, z0, time_value = params
    return C0 * (1 - erf((z - z0) / (2 * np.sqrt(D * time_value))))

# Load data from Excel file with depth in the first column and concentration in subsequent columns
data = pd.read_excel("D:\\LuXY\\Desktop\\Diffusion\\Data.xlsx", header=None, skiprows=1)

# Let the user input the time value in days
time_value_days = float(input("Enter the time value in days: "))
time_value = time_value_days * 24 * 60 * 60  # Convert days to seconds

depths_mm = pd.to_numeric(data.iloc[:, 0], errors='coerce').values
depths_m = depths_mm / 1000  # Convert depths to meters

# Extract concentration data for all time points
concentration_data = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').values

if np.any(np.isnan(concentration_data)):
    print("Non-numeric values found in concentration data, please check your input.")
    exit()

# Initial guess for curve fitting
initial_guess = [1e-15, np.nanmax(concentration_data), max(depths_m), time_value]

# Fit the diffusion model to the data for each time point
plt.figure(figsize=(10, 6))
for i in range(concentration_data.shape[1]):
    concentrations = concentration_data[:, i]
    popt, _ = curve_fit(fick_second_law, depths_m, concentrations, p0=initial_guess, bounds=(0, np.inf))
    D_best_fitted = popt[0]
    
    # Generate the fitted curve for the current time point
    x_range = np.linspace(0, max(depths_m), num=100)  # Start from x=0
    y_fit = fick_second_law(x_range, *popt)
    
    # Plot the experimental data and the fitted curve for the current time point
    plt.plot(depths_mm, concentrations, 'o')
    plt.plot(x_range * 1000, y_fit, label=f'Diffusion Fit ({i+1}), D = {D_best_fitted:.2E} m²/s, C$_0$ = {popt[1]:.2f}')  # Include C0 for x=0

plt.xlabel('Depth (mm)', fontsize=14)
plt.ylabel('Concentration (%)', fontsize=14)
plt.title(f'Concentration Profiles at {time_value_days} days', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend(fontsize=12, frameon=False)  # Remove legend box

plt.grid(False)  # Remove grid
#plt.xlim(0, max(depths_mm))  # Set x-axis limits from 0 to the maximum depth
#plt.ylim(0, np.nanmax(concentration_data))  # Set y-axis limits from 0 to the maximum concentration

plt.savefig('depth_con_fit.png', dpi=300)
#plt.close()
plt.show()

print("Diffusion coefficient calculation and plotting completed.")
