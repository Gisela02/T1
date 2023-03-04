import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd 
from numpy.fft import fft 

T= 0.025                               
x_r, fm =sf.read('Gorilla.wav')       
L = int(fm * T)                     
Tm=1/fm                            
t=Tm*np.arange(L)                  
sf.write('exercici4.wav', x_r, fm)  

plt.figure(4)                          
plt.plot(t[0:L],x_r[0:L])              
plt.xlabel('t en segons')               
plt.title('Exercici 4')  
plt.show()  
sd.play(x_r, fm)

N=5000                        
X=fft(x_r[0 : L], N)    
k=np.arange(N)                                         
plt.figure(42)                         
XdB = 20*np.log10(1.e-1 + np.abs(X)/(max(np.abs(X))))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)   
plt.plot(fk,XdB[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                   
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')          
plt.show() 