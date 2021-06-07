import numpy as np
import matplotlib.pyplot as plt

f0 = 440

factor  = np.array([2 ** i for i in range(1,5)])

lower_octaves = f0 / factor
higer_octaves = f0 * factor

octaves = np.concatenate([lower_octaves[::-1],[f0],higer_octaves])

print(octaves,'\n')

octave_deltas = np.array([octaves[i] - octaves[i-1] for i in range(1,len(octaves))])

print(octave_deltas,'\n')

def twelth(delta=440):
	pow = np.arange (0,11)
	beta = np.power(2,1/12)
	
	note_intervals = delta[:,np.newaxis] * np.array(np.power(beta,pow))
	
	return np.array(note_intervals).flatten()
		
	
key_freq = twelth(octave_deltas)
print((key_freq))

key_interval = np.array([key_freq[i] - key_freq[i-1] for i in range(1,len(key_freq))])

print(key_interval)

fig,axes = plt.subplots(2,sharex=True)
axes[0].plot(key_freq,'o--')
axes[0].grid(True)
axes[0].set_xlabel('piano key')
axes[0].set_ylabel('frequency')
axes[0].set_yscale('log')

axes[1].plot(key_interval,'o--')
axes[1].grid(True)
axes[1].set_ylabel('key freq. delta')
axes[1].set_xlabel('key_interval')
plt.show()


