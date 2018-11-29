#from logmmse import logmmse_from_file
from logmmse import logmmse
from wav_rw import wavread, wavwrite
import matplotlib.pyplot as plt


rate,sig = wavread('noisy_audio.wav')
print rate
#graficar senal original
plt.subplot(311)
plt.plot(sig)

#graficar un caso usando parametros por defecto
sig_n=logmmse(sig,rate, initial_noise=6, window_size=0, noise_threshold=0.25)
plt.subplot(312)
plt.plot(sig_n)
wavwrite(sig_n,rate,'clean1.wav')

#graficar un caso usando parametros por defecto
sig_n=logmmse(sig,rate, initial_noise=3, window_size=0, noise_threshold=0.05)
wavwrite(sig_n,rate,'clean2.wav')
plt.subplot(313)
plt.plot(sig_n)

plt.show()
