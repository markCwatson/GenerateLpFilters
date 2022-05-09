# By Mark Watson, Summer 2021

# Example usage: py LpFlters.py 4 1 8
# where Fs = 4, cutoff = 1, # taps = 8
# Will generate LPF coefficients for FIR and moving average.

from pylab import *
from scipy.signal import windows, firwin
import sys


Fs = float(sys.argv[1])
cutoff = float(sys.argv[2])
N = int(sys.argv[3])

h_lpf = firwin(N, cutoff=cutoff, window='hamming', pass_zero=True, fs=Fs)
h_ma = ones(N)*1./N

print("LPF coefficients = ")
print(h_lpf)

print("MA coefficients = ")
print(h_ma)

M = 512
f = arange(M)*Fs/M - Fs/2.0

X_lpf = fftshift(abs(fft(h_lpf, M)))
X_ma = fftshift(abs(fft(h_ma, M)))

figure()
plot(f, X_lpf, f, X_ma)
xlabel('$f$ (Hz)')
ylabel('$|H(f)|$')
legend(('LPF', 'Moving Average'))
grid()
show()