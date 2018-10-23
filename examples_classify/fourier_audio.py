#Milton Orlando Sarria
#analisis espectral de sinusoides

import matplotlib.pyplot as plt
import numpy as np
from python_speech_features import fbank
from wav_rw import wavread

import h5py

lista='lista.txt'
hf = open(lista,'r')
lines=hf.readlines()
hf.close()
archivo=open('lista_feats.txt','w')
#calc. log filter bank energy
for line in lines:
    audio,label=line.split('\t')
    (rate,sig) = wavread(audio)    
    feat,e = fbank(sig,samplerate=rate, nfilt=19, nfft=2048, lowfreq=100,highfreq=8000, winfunc=np.hamming)
    #apply logarithm
    fbank_log=np.log(feat)        
    file_feat ='feats/'+audio.split('/')[-1:][0].split('.')[0] + '.h5'
    hf = h5py.File(file_feat, "w") #handle file
    dset = hf.create_dataset('fbank', data=fbank_log)
    dset = hf.create_dataset('label', data=int(label))
    hf.close()
    
    linea = file_feat + '\n' 
    archivo.write(linea)
        
archivo.close()
   
