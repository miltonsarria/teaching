#Milton Orlando Sarria
#calcular log fbank feats

import matplotlib.pyplot as plt
import numpy as np
from python_speech_features import fbank
from wav_rw import wavread
from scipy import signal
import h5py
from pandas import Series


lista='lista_isolated.txt'
hf = open(lista,'r')
lines=hf.readlines()
hf.close()
archivo=open('lista_feats_isolated.txt','w')
#calc. log filter bank energy
naverage = 10

for line in lines:
    audio,label=line.split('\t')
    print label
    (rate,sig) = wavread(audio)    
    feat,e = fbank(sig,samplerate=rate, nfilt=19, nfft=2048, lowfreq=100,highfreq=8000, winfunc=np.hamming)
    #apply logarithm
    fbank_log=np.log(feat) 
    
    e[e < np.finfo(float).eps] = np.finfo(float).eps
    logE=np.log(e)
    s=Series(logE)
    logE = (s.rolling(window=naverage)).mean().values
    logE[0:naverage-1]=logE[naverage:].min()
    logE=np.roll(logE, -naverage/2, axis=0)
    
    #nle = signal.resample(logE,10*rate)
    #ne = signal.resample(e,10*rate)
    #plt.plot(sig[0:10*rate]); plt.plot(ne); plt.plot(nle); 
    #plt.show()
    
    tresh=logE>-7
    segmentos=np.hstack((tresh,0))-np.hstack((0,tresh))
    start   = np.arange(segmentos.size)[segmentos>0]
    end     = np.arange(segmentos.size)[segmentos<0]
    count=1
  
    for a,b in zip(start,end):
        file_feat ='feats/'+audio.split('/')[-1:][0].split('.')[0]+ '_'+ str(count) + '_.h5'
        hf = h5py.File(file_feat, "w") #handle file
        
        dset = hf.create_dataset('fbank', data=fbank_log[a:b,:])
        dset = hf.create_dataset('label', data=int(label))
        hf.close()
    
        linea = file_feat + '\n' 
        archivo.write(linea)
        count+=1
archivo.close()
   
