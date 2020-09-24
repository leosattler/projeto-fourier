#========================================================================
#                                 IMPORTS
#------------------------------------------------------------------------
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
#========================================================================
#                           FUNCOES AUXILIARES
#------------------------------------------------------------------------
def tratamento_jump(data, times_media=5):
    m = np.mean(data)
    data[np.where(data>times_media*m)] = m
#========================================================================
#                                  SINAIS
#------------------------------------------------------------------------
years = np.arange(1964, 2020)
#-------------------------------------
f1_file=np.genfromtxt('dailyaveraged_data.txt')
f1_year = f1_file[1:, 0]
f1_doy = f1_file[1:, 1]
f1_data = f1_file[1:, 3]
tratamento_jump(f1_data, 5)
f1 = []
k=0
for y in years:
    c = 0
    for i in np.arange(0, len(f1_data)):
        if int(f1_year[i]) == int(y) and c<=365:
            d = f1_data[i]
            f1.append(d)
            c=c+1
        if c>=365:
            break
#-------------------------------------
f2_file = np.genfromtxt('27dayaveraged_data.txt')
f2_year = f2_file[1:, 0]
f2_doy = f2_file[1:, 1]
f2_data = f2_file[1:, 3]
f2 = []
k=0
for y in years:
    c=0
    for i in np.arange(0, len(f2_data)):
        if int(f2_year[i]) == int(y) and c<=12:
            d = f2_data[i]
            f2.append(d)
            c=c+1
        if c>=12:
            break
#-------------------------------------
f3_file = np.genfromtxt('yearlyaveraged_data.txt')
f3_year = f3_file[1:, 0]
f3_doy = f3_file[1:, 1]
f3_data = f3_file[1:, 3]
f3 = np.array(f3_data)[:-1]
#========================================================================
#                               PLOTS (tempo)
#------------------------------------------------------------------------
plt.figure(figsize=[15,7])
#-------------------------------------
plt.subplot(3,2,1)
plt.title('Solar index F10.7')
plt.plot(f1, 'r-')
plt.ylabel('Daily   \naveraged', rotation='horizontal', ha='right')
#-------------------------------------
plt.subplot(3,2,3)
plt.ylabel('27-day  \naveraged', rotation='horizontal', ha='right')
plt.plot(f2, 'b-')
#-------------------------------------
plt.subplot(3,2,5)
plt.ylabel('Yearly  \naveraged', rotation='horizontal', ha='right')
plt.plot(f3, 'g-')
#========================================================================
#                                 ESPECTROS
#------------------------------------------------------------------------
# Truncando dados (ate a maior potencia de 2 possivel)
N1 = 2**14 #len(f1)
N2 = 512 #len(f2)
N3 = 32 #len(f3)
# Realizando a DFT via FFT
ft1 = fft.fft(f1, N1)/N1
ft2 = fft.fft(f2, N2)/N2
ft3 = fft.fft(f3, N3)/N3
# Zerando primeiro termo do output (igual a soma da serie)
ft2[0] = 0
ft1[0] = 0 
ft3[0] = 0
# Realizando o shift sobre os outputs (para o centro
ft1_shifted = fft.fftshift(ft1)
ft2_shifted = fft.fftshift(ft2)
ft3_shifted = fft.fftshift(ft3)
# Espectro de potencia com shift
aft1_shifted = abs(ft1_shifted)**2
aft2_shifted = abs(ft2_shifted)**2
aft3_shifted = abs(ft3_shifted)**2
#aft1 = np.abs(ft1)**2
#aft2 = np.abs(ft2)**2
#aft3 = np.abs(ft3)**2
#========================================================================
#                             PLOTS (frequencia)
#------------------------------------------------------------------------
# Frequancias para o eixo horizontal
xt1_shifted = 365*np.arange(-N1/2,N1/2)/float(N1)
xt2_shifted = 12*np.arange(-N2/2,N2/2)/float(N2)
xt3_shifted = np.arange(-N3/2,N3/2)/float(N3)
#-------------------------------------
plt.subplot(3,2,2)
plt.title('Normalized Power Spectrum')
plt.plot(xt1_shifted, aft1_shifted, 'r-')
plt.xlim(0,.4)
#-------------------------------------
plt.subplot(3,2,4)
plt.plot(xt2_shifted, aft2_shifted, 'b-')
plt.xlim(0,.4)
#-------------------------------------
plt.subplot(3,2,6)
plt.plot(xt3_shifted, aft3_shifted, 'g-')#, label = str(t_1) + ' + ' + str(t_2) + ' periodos')
plt.xlim(0,.4)
#-------------------------------------
plt.subplots_adjust(hspace=.4)
plt.savefig('final_ff.jpg', dpi=400, bbox_inches='tight')
plt.show()
#========================================================================
