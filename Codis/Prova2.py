import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft 

x_r, fm = sf.read('exercici1.wav')

T = 2.5                           
fx=523                              
A=4 
pi=np.pi 
L = int(fm * T)                     
Tm=1/fm                              
t=Tm* np.arange(len(x_r)) 
x = A * np.cos(2 * pi * fx * t)   
sf.write('exercici2.wav', x, fm) 

fx=fm/2
Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(2)                             
plt.plot(t[0:Ls], x_r[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show() 

sd.play(x_r, fm) 

N=5000                        
X=fft(x_r[0 : Ls], N)  
k=np.arange(N)

plt.figure(21)
plt.subplot(211) 
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|') 
plt.subplot(212) 
plt.plot(k,np.unwrap(np.angle(X))) 
plt.xlabel('Index k')               
plt.ylabel('$\phi_x[k]$') 
plt.show() 