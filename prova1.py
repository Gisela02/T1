import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

T= 2.5                              
fm=8000                              
fx=4000                               
A=4                                  
pi=np.pi                             
L = int(fm * T)                     
Tm=1/fm                              
t=Tm*np.arange(L)                   
x = A * np.cos(2 * pi * fx * t)      
sf.write('exercici1.wav', x, fm)   