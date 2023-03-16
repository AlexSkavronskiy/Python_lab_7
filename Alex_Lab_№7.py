import csv
import numpy as np
import matplotlib.pyplot as plt
import math

allVallues = []  # Все значения
g = []

with open('data2.csv', mode='r') as file:
    csv = csv.reader(file)
    for lines in csv:
        g.append(lines[3])

for i in g[1:len(g)]:  # Записываем все значения без названия строки
    allVallues.append(float(i))


def normalize(arr, tmin, tmax):  # функция для подсчета нормализованного распределения
    norm_arr = []
    diff = tmax - tmin
    diff_arr = max(arr) - min(arr)
    for i in arr:
        temp = (((i - min(arr)) * diff) / diff_arr) + tmin
        norm_arr.append(temp)
    return norm_arr


range_to_normalize = (0, 1)
normalized_allValues = normalize(allVallues, range_to_normalize[0],
                                 range_to_normalize[1])  # считаем нормализованного распределения
sigma = np.std(allVallues)  # считаем среднеквадратичное значение

fig, axs = plt.subplots(1, 2, tight_layout=True, figsize=(12, 6))

axs[0].axvline(x=sigma, color='r')
axs[0].text(2, 150, 'среднеквадратичное значение', rotation='vertical')
axs[0].hist(allVallues, bins=24, edgecolor='black')
axs[1].hist(normalized_allValues, bins=24, density=True, color='green', edgecolor='black')

axs[0].set_xlabel('Значение измерений')
axs[0].set_ylabel('Интегральное значение')

axs[1].set_xlabel('Значение измерений')
axs[1].set_ylabel('Интегральное значение')

axs[0].set_title('Распределение Chloramines')
axs[1].set_title('Нормализованное распределение Chloramines')

fig = plt.figure(2)
ax = plt.axes(projection='3d')
x = np.linspace(-3 * math.pi, 3 * math.pi)
y = np.cos(x)
z = x / np.sin(x)
ax.plot3D(x, y, z, 'red')
ax.set_title('График задания номер 3')
ax.set_xlabel('Ось x')
ax.set_ylabel('Ось y')
ax.set_zlabel('Ось z')

plt.show()
