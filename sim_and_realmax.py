import numpy as np
import matplotlib.pyplot as plt

magnitudes = []
maxes = []
for i in range(1975, 2018):
    with open(str(i) + '.txt') as f:
        for line in f:
            magnitudes.append(float(line[:len(line)-1]))
        maxes.append(max(magnitudes))
        magnitudes = []  

plt.hist(np.asarray(maxes), 'auto', color = 'c', histtype = 'step')

avgHist = []

for j in range(100):
    magnitudes = []
    i = 0
    num_of_years = 44
    while i < num_of_years:
        magnitude = max(np.random.exponential(scale = 1/2.2, size = 3000))
        magnitudes.append(magnitude + 2)
        i += 1

    histi = np.histogram(np.asarray(magnitudes), bins = np.arange(3,9,.33))
    avgHist.append(histi[0])
avgHist = np.array(avgHist)

plt.step(np.arange(3,8.67,.33), np.average(avgHist, axis = 0))
plt.xlabel('Magnitude')
plt.ylabel('# of Occurences')
plt.title('Real vs Simluated Histogram of Maximum Magnitudes')

plt.savefig('b.png', transparent = True)
