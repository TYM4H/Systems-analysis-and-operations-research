import matplotlib.pyplot as plt

n_values = [1000, 2000, 5000, 10000]
bubble_times = [0.011040, 0.056828, 0.318273, 1.257788]
sorted_times = [0.000059, 0.000125, 0.000371, 0.000726]

plt.figure(figsize=(10,6))
plt.plot(n_values, bubble_times, marker='o', label='Bubble sort', color='red')
plt.plot(n_values, sorted_times, marker='o', label='Python sorted()', color='green')
#plt.yscale('log')
plt.xlabel('Размер массива n')
plt.ylabel('Время сортировки (секунды, log scale)')
plt.title('Сравнение пузырьковой сортировки и Python sorted()')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
