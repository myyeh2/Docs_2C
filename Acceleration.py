import numpy as np 
import matplotlib.pylab as plt 

#Time Series 
x = np.arange(0, 20.25, 0.25)

#y0_Acceleration Data
y0= [ 
-0.00001,  -3.06865,  -3.91924,  -1.90291,  1.59692,  
4.13427,  3.92096,  1.08615,  -2.41207,  -4.16093,  
-2.98595,  0.22894,  3.17096,  3.73331,  1.50325,  
-1.94513,  -4.15996,  -3.54126,  -0.47276,  2.94195,  
4.3538,  2.81575,  -0.55606,  -3.37252,  -3.65585,  
-1.23187,  2.15049,  4.05613,  3.08526,  -0.13356,  
-3.3793,  -4.39701,  -2.48209,  1.02494,  3.68159,  
3.66015,  1.02961,  -2.29966,  -3.92842,  -2.6651,  
0.62954,  3.64501,  4.24715,  1.9824,  -1.59904,  
-4.02951,  -3.655,  -0.79295,  2.49801,  3.8732,  
2.35652,  -0.97113,  -3.73471,  -3.9416,  -1.39072,  
2.17902,  4.30628,  3.53423,  0.43145,  -2.81159,  
-3.92586,  -2.15997,  1.19476,  3.71966,  3.57907,  
0.82022,  -2.65356,  -4.41847,  -3.23445,  0.08186,  
3.23009,  4.0419,  2.00209,  -1.39562,  -3.70759,  
-3.26758,  -0.36492,  2.95668,  4.33845,  2.77016,  
-0.69378, 
] 

#y1_Acceleration Data 
y1 = [ 
0,       1.77915,  2.41899,  1.56854,  -0.1,    
-1.3737,   -1.35785,  -0.1058,  1.42387,  2.05191,  
1.22157,  -0.59516,  -2.21599,  -2.56899,  -1.43891,  
0.38535,  1.66549,  1.58013,  0.29344,  -1.17342,  
-1.67566,  -0.76496,  0.9831,  2.36626,  2.39875,  
1.00696,  -0.91239,  -2.11353,  -1.86584,  -0.4542,  
1.03536,  1.49184,  0.56943,  -1.06597,  -2.2077,  
-1.96501,  -0.40107,  1.49816,  2.50406,  1.99713,  
0.39233,  -1.16036,  -1.58829,  -0.649,  0.90631,  
1.87293,  1.4546,  -0.16137,  -1.92279,   -2.64298,  
-1.82985,  -0.03063,  1.55041,   1.89232,  0.86505,  
-0.69265,  -1.5782,  -1.08522,  0.48878,  2.04576,  
2.45919,  1.37115,  -0.54733,  -2.05709,  -2.2097,  
-1.00121,  0.63787,  1.50775,  0.98993,  -0.51644,  
-1.87995,  -2.04248,  -0.77653,  1.14059,  2.46007,  
2.32857,  0.87979,  -0.86472,  -1.71523,  -1.14687,  
0.33986,  
] 

plt.figure(figsize = (8, 4)) 
plt.subplots_adjust(bottom = 0.2, left = 0.2) 

plt.plot(x, y0, 'r-', label = r'$Point_0$', lw = 2) 
plt.plot(x, y1, 'b-', label = r'$Point_1$', lw = 2)  

plt.xlabel(r'$Time(Sec)$').set_fontsize(16)  
plt.ylabel(r'$Amplitude$').set_fontsize(16) 
plt.title(r'$***Time*and*Acceleration***$').set_fontsize(16) 

plt.grid(axis = 'both') 
plt.legend(loc = 'best') 

plt.show() 