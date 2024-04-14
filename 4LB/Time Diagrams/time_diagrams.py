import numpy as np
import matplotlib.pyplot as plt

# Функция для генерации прямоугольного сигнала
def generate_square_wave(period, pulse_width, amplitude, total_time):
    t = np.linspace(0, total_time, 1000)
    signal = amplitude * (t % period < pulse_width)
    return t, signal

# Построение диаграммы для каждого сигнала
amplitude = 3
signals = [(4, 8), (2, 8), (1, 8), (2, 4), (2, 16), (2, 32), (2, 64)] 
for n, signal_params in enumerate(signals):
    total_time = signal_params[1] * 3
    t, signal = generate_square_wave(signal_params[1], signal_params[0], amplitude, total_time)

    # Построение диаграммы
    plt.figure(figsize=(16, 9))
    plt.plot(t, signal)
    plt.xlabel('Time, mks')
    plt.ylabel('Amplitude, V')
    plt.title(f'Signal {n+1}')
    plt.grid(True)
    
    # Сохранение графика в файл в формате PNG
    plt.savefig(f'signal_{n+1}.png')
    plt.close()