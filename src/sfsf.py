import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
fs = 1000  # sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# FFT
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft_vals), 1/fs)

# Plot
plt.plot(freqs[:len(freqs)//2], np.abs(fft_vals[:len(fft_vals)//2]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of Signal")
plt.show()