import os 
import matplotlib.pyplot as plt
import numpy as np
import wav_process as wp
data_dir='/home/sarria/python/audio/audio'
######################
# frequency range to plot
maxplotfreq = 5000.0
for dirpath, dirnames, filenames in os.walk(data_dir):
   for name in filenames:
      if name.split('.')[1]=='wav':
         fullname = os.path.join(dirpath,name)
         
         print 'reading: ' + fullname
         (fs,x)=wp.wavread(fullname)
         print 'sampling rate: ' + str(fs) + ', number of data points: ' + str(x.size)

         #using a sampling rate of 16k you can define a window size of 25ms, and hop size of 10ms
         #it results in frames of 400 data points and 160 data points of increment
         M = int(fs * 0.025)
         H = int(fs * 0.010)
         N = 512
         #window choice of rectangular, hanning, hamming, blackman, blackmanharris
         (X,mX)=wp.enframe(x=x, window = 'hamming', M=M, H=H)
         
         # plot the input sound
         plt.subplot(2,1,1)
         plt.plot(np.arange(x.size)/float(fs), x)
         plt.axis([0, x.size/float(fs), min(x), max(x)])
         plt.ylabel('amplitude')
         plt.xlabel('time (sec)')
         plt.title('input sound: x')
         

         
         # plot magnitude spectrogram
         plt.subplot(2,1,2)
         numFrames = int(X[:,0].size)
         frmTime = H*np.arange(numFrames)/float(fs)                             
         binFreq = fs*np.arange(N*maxplotfreq/fs)/N  
         plt.pcolormesh(np.transpose(mX[:,:int(N*maxplotfreq/fs+1)]))
         plt.xlabel('time (sec)')
         plt.ylabel('frequency (Hz)')
         plt.title('magnitude spectrogram')
         plt.autoscale(tight=True)
         
         plt.show()
         
         
         print X.shape, M, H
         
         



