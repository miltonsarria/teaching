# function to chop into small segments a signal

import numpy as np
import os, sys
from scipy.signal import get_window


def enframe(x = None, window = 'hamming', M = 1024, H = 512):
        """
        inputs:
        x       input signal
        window  analysis window type (choice of rectangular, hanning, hamming, blackman, blackmanharris)         
        N       analysis window size 
        H       hop size (at least 1/2 of analysis window size to have good overlap-add) 
        output:
        X       np array with frames
        """
        if (x is None):                 # raise error if there is no input signal
           raise ValueError("there is no input signal")
                     
        # compute analysis window
        w    = get_window(window, M)
        pin  = 0                                        # the sound pointer starts at the sample 0
        pend = x.size-M                                 # last sample to start a frame
        w    = w / sum(w)                               # normalize analysis window
        while pin<=pend:                                # while sound pointer is smaller than last sample      
             x1 = x[pin:pin+M]                       # select one frame of input sound
             if (w.size != x1.size):                 # raise error if window size is different to frame size
                   raise ValueError("Window size (M) is different of frame size")
             xw = x1*w                               # window the frame
             if pin == 0:                            # if first frame, create output array
                   X = np.array([xw])
             else:                                   # append output to existing array 
                   X = np.vstack((X,np.array([xw])))
             pin += H                                # advance sound pointer

        return X

