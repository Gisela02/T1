import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft 

T= 2.5                              
fm=8000                              
fx=4000                               
A=4                                  
pi=np.pi                             
L = int(fm * T)                     
Tm=1/fm                              
t=Tm*np.arange(L)                   
x = A * np.cos(2 * pi * fx * t)      
sf.write('exercici3.wav', x, fm)  
x_r, fm = sf.read('exercici3.wav')
Tx=1/fx                                   
Ls=int(fm*5*Tx) 

plt.figure(3)                             
plt.plot(t[0:Ls], x[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('Ex 3')  
plt.show() 

sd.play(x, fm)

N=5000                        
X=fft(x[0 : Ls], N)  
k=np.arange(N)

plt.figure(31)

XdB = 20*(np.log10(np.abs(X)/max(np.abs(X))))
fk = (k/N)*fm
                        
plt.subplot(211)
 
plt.plot(fk,XdB)                   
plt.title('Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(XdB)))    
plt.xlabel('fk (Hz)')                  
plt.ylabel('$\phi_x[k]$')    
plt.show() 


