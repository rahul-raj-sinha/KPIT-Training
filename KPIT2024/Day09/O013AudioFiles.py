
import wave
import numpy as np
import matplotlib.pyplot as plt

audFile = wave.open("C:\Training\PycharmProjects\KPIT2024\Day09\harvard.wav", "rb")

samplefreq = audFile.getframerate()
n_samples = audFile.getnframes()
t_audio = n_samples / samplefreq
n_channels = audFile.getnchannels()

signal_wave = audFile.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=int)

print("The signal contains a total of " + str(signal_array[0]) + " samples ")
print("If this value is greater than " + str(str(n_samples) + " it is due to there being multiple channels"))

print("Eg: -Samples * Channels = " + str(n_samples * n_channels))

l_channel = signal_array[0:2]
r_channel = signal_array[1:2]

print("-" * 60)

timestamps = np.linspace(0, n_samples/samplefreq, num=n_samples)

plt.figure(figsize=(10, 5))
plt.plot(timestamps, r_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

# https://www.kaggle.com/code/birdy654/visualising-audio-data-in-python
# https://learnpython.com/blog/plot-waveform-in-python/