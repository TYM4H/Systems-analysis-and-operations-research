# Данные 5 экспериментов
data = {
    100:  [0.000131, 0.000104, 0.000136, 0.000145, 0.000106],
    200:  [0.000482, 0.000483, 0.000425, 0.000454, 0.000323],
    400:  [0.002028, 0.001816, 0.001454, 0.001812, 0.001495],
    800:  [0.008329, 0.006443, 0.006633, 0.007042, 0.006454],
    1600: [0.029510, 0.031749, 0.034052, 0.038426, 0.033466],
    3200: [0.123648, 0.151313, 0.115664, 0.125193, 0.138443],
}

import matplotlib.pyplot as plt
import numpy as np

sizes = sorted(data.keys())
avg_times = [np.mean(data[n]) for n in sizes]

n_vals = np.array(sizes)
n2_vals = n_vals ** 2

# Масштабируем n и n^2 к первому значению времени
scale_n = avg_times[0] / n_vals[0]
scale_n2 = avg_times[0] / n2_vals[0]

linear_model = scale_n * n_vals
quadratic_model = scale_n2 * n2_vals

plt.figure()
plt.plot(n_vals, avg_times, label="Экспериментальные данные")
plt.plot(n_vals, linear_model, label="O(n)")
plt.plot(n_vals, quadratic_model, label="O(n²)")

plt.xlabel("Размер массива (n)")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение: эксперимент, O(n), O(n²)")
plt.legend()
plt.show()

for n, t in zip(sizes, avg_times):
    print(f"n = {n:<5} среднее время = {t:.6f} сек")
