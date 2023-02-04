import matplotlib.pyplot as plt
import pyedflib
import numpy as np
import pandas as pd

f = pyedflib.EdfReader('n16.edf')
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))
for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
print(f.getSampleFrequencies())
fs = 100
l = 1000
amp = 2*np.sqrt(2)
t =  np.arange(0,l)*1/fs
print("Labels: ", signal_labels, len(signal_labels),"\n--------------\n")

signal1 = sigbufs[0,:] #Fp2-F4
signal2 = sigbufs[1,:] #F4-C4
signal3 = sigbufs[2,:] #C4-P4
signal4 = sigbufs[3,:] #P4-O2
signal5 = sigbufs[4,:] #C4-A1

plt.figure(figsize=(15,10))
plt.subplot(511)
plt.plot(t,signal1[:l])
plt.title('Fp2-F4')
#------------------
plt.subplot(512)
plt.plot(t,signal2[:l])
plt.title('F4-C4')
#------------------
plt.subplot(513)
plt.plot(t,signal3[:l])
plt.title('C4-P4')
#------------------
plt.subplot(514)
plt.plot(t,signal4[:l])
plt.title('P4-O2')
#------------------
plt.subplot(515)
plt.plot(t,signal5[:l])
plt.title('C4-A1')
#------------------
plt.show()
#-----------------
#Dyskretna tranformata Fouriera
signal1t = np.absolute(np.fft.rfft(signal1))
signal2t = np.absolute(np.fft.rfft(signal2))
signal3t = np.absolute(np.fft.rfft(signal3))
signal4t = np.absolute(np.fft.rfft(signal4))
signal5t = np.absolute(np.fft.rfft(signal5))
#-----------------
#Częstotliwości próbek
freq1 = np.fft.rfftfreq(len(signal1),1/fs)
freq2 = np.fft.rfftfreq(len(signal2),1/fs)
freq3 = np.fft.rfftfreq(len(signal3),1/fs)
freq4 = np.fft.rfftfreq(len(signal4),1/fs)
freq5 = np.fft.rfftfreq(len(signal5),1/fs)
#-----------------

#Wizualizacja
plt.figure(figsize=(15,20))
plt.subplot(511)
plt.plot(freq1[1:1000],abs(signal1t[1:1000]))
plt.title('Fp2-F4')
#------------------
plt.subplot(512)
plt.plot(freq2[1:1000],abs(signal2t[1:1000]))
plt.title('F4-C4')
#------------------
plt.subplot(513)
plt.plot(freq3[1:1000],abs(signal3t[1:1000]))
plt.title('C4-P4')
#------------------
plt.subplot(514)
plt.plot(freq4[1:1000],abs(signal4t[1:1000]))
plt.title('P4-O2')
#------------------
plt.subplot(515)
plt.plot(freq5[1:1000],abs(signal5t[1:1000]))
plt.title('C4-A1')
#------------------
plt.show()
#-----------------
#Przedziały częstotliwości
eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (8, 12),
             'Beta': (12, 30),
             'Gamma': (30, 100)}


#Sprawdzanie częstotliwości dla odpowiednich przedziałów i wizualizacja wyników
#'Fp2-F4'
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((freq1 >= eeg_bands[band][0]) &
                       (freq1 <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(signal1t[freq_ix])

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_title('Fp2-F4')
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")
plt.show()
#-----------------
#'F4-C4'
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((freq2 >= eeg_bands[band][0]) &
                       (freq2 <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(signal2t[freq_ix])

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_title('F4-C4')
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")
plt.show()
#-----------------
#'C4-P4'
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((freq3 >= eeg_bands[band][0]) &
                       (freq3 <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(signal3t[freq_ix])

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_title('C4-P4')
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")
plt.show()
#-----------------
#'P4-O2'
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((freq4 >= eeg_bands[band][0]) &
                       (freq4 <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(signal4t[freq_ix])

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_title('P4-O2')
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")
plt.show()
#-----------------
#'C4-A1'
eeg_band_fft = dict()
for band in eeg_bands:
    freq_ix = np.where((freq5 >= eeg_bands[band][0]) &
                       (freq5 <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(signal5t[freq_ix])

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_title('C4-A1')
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")
plt.show()
#-----------------