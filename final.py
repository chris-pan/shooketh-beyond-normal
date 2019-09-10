"""
UCI COSMOS
Cluster 2: Beyond Normal
Jeffrey Chen, Daisy Cui, Christopher Pan, Amber Sun, Chengxuan Wang
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

# Reads earthquake data between 1975 and 2018 from http://service.scedc.caltech.edu/ftp/catalogs/SCEC_DC/ 

file_suffix = ".txt"
magnitudes = np.asarray([])
start_year = 1975
end_year = 2017
# Since smaller earthquakes (i.e. less than 1.6) are often missed and go unrecorded, we limit our data to magnitudes greater than 1.6. 

# A rough exponential distribution that we try to fit our data to.
for i in range(1975, 2017):
    my_data = np.genfromtxt(str(i) + '.csv', delimiter=',', usecols=np.arange(4,5), dtype=None)
    magnitudes = np.append(my_data[1:].astype(np.float), magnitudes)
    
print(magnitudes)
magnitudes = np.delete(magnitudes, np.where(magnitudes < 1.6))
magnitudes = np.round(magnitudes,2)
hist = plt.hist(magnitudes , bins = "auto", edgecolor = 'c')
def exponential_dist(x,lamda, translation):
    return math.e**(-lamda*(x-translation))

    
popt, pcov = curve_fit(exponential_dist,hist[1][0:-1],hist[0])

print("[λ, translation]: " + str(popt))
l = popt[0] # Lambda
l = round(l, 4)
t = popt[1] # Translation 

# Calculations using lambda
# For an exponential distribution, the median is 1/lambda * (ln (n) - ln(ln(2))), where n is the number of years.
# As a result, the median grows with n at a logarithmic rate. 
start_year = 1985
end_year = 2018
num_of_eq = len(magnitudes)
print("Between " + str(start_year) + " and " + str(end_year - 1) + ", " + str(num_of_eq) + " earthquakes were recorded.")
num_years = end_year - start_year
average_yearly_eq = num_of_eq / num_years
print("Average number of earthquakes a year: " + str(average_yearly_eq))
def calculate_median(num_of_eq):
    return 1/l * (math.log(num_of_eq) - math.log(math.log(2)))

mag = 7
temp_eq = average_yearly_eq
while (calculate_median(temp_eq) <= mag):
    temp_eq+= average_yearly_eq

print("After " + str(temp_eq) + " more earthquakes, " + " there is a 50/50 chance of having an earthquake of magnitude " + str(mag) + ".")
print("In other words, we can expect a " + str(mag) + " magnitude earthquake once every " + str(temp_eq/average_yearly_eq) + " years.")

# Graph exponential distribution

x = np.linspace(1.5,7, 50)
y = np.exp(-l * (x - t))
plt.plot(x,y, color = "black")
plt.xlabel("Magnitude")
plt.ylabel("Occurrences")
plt.title("United States Earthquakes Between 1985 and 2017", y=1.04)
plt.text(3, 7500, r'$\lambda$' + " = " + str(l))
plt.savefig('norcal.png', transparent=True)
