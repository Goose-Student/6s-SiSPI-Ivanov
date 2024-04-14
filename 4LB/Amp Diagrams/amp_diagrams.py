import numpy as np
import matplotlib.pyplot as plt

# Функция для генерации прямоугольного сигнала
def generate_square_wave(period, pulse_width, amplitude, total_time):
    t = np.linspace(0, total_time, 1000)
    signal = amplitude * (t % period < pulse_width)
    return t, signal

# Функция для вычисления и построения амплитудного спектра
def plot_amplitude_spectrum(t, signal, total_time):
    n = len(t)
    dt = total_time / n 
    # Вычислить частоты, соответствующие каждой точке в дискретном пространстве частот
    frequency = np.fft.fftfreq(n, dt)
    
    # Преобразование Фурье переводит сигнал из временной области в частотную область
    signal_fft = np.fft.fft(signal) 

    amplitude_spectrum = np.abs(signal_fft) / n
    frequencies_positive = frequency[:n//2]
    amplitude_spectrum_positive = amplitude_spectrum[:n//2]

    # Построение амплитудного спектра
    plt.figure(figsize=(16, 9))
    plt.plot(frequencies_positive, amplitude_spectrum_positive)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title(f'Amplitude Spectrum signal')
    plt.grid(True)
    return plt

# Параметры для каждого сигнала (pulse_width, period)
signals = [(4, 8), (2, 8), (1, 8), (2, 4), (2, 16), (2, 32), (2, 64)]
amplitude = 3
for n, signal_params in enumerate(signals):
    total_time = signal_params[1] * 8
    t, signal = generate_square_wave(signal_params[1], signal_params[0], amplitude, total_time)

    # Построение амплитудного спектра для каждого сигнала
    diagram = plot_amplitude_spectrum(t, signal, total_time)
    diagram.savefig(f'signal_{n+1}.png')
    diagram.close()