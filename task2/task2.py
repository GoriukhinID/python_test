from math import sqrt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys


def find_points(d1, d2, R, line1):
    """Функция решает квадратное уравнение относительно параметра t,
    заданного в уравнении прямой, подставляет эти значения в уравнение
    прямой и выдаёт точки пересечения сферы и прямой."""
    # Объявляем параметры квадратного уравнения
    a = d1[0]**2 + d1[1]**2 + d1[2]**2
    b = 2*(d1[0]*d2[0] + d1[1]*d2[1] + d1[2]*d2[2])
    c = d2[0]**2 + d2[1]**2 + d2[2]**2 - R**2
    disc = b**2 - 4*a*c
    epsilon = 0.00000001
    # Точек нет
    if disc + epsilon < 0:
        print("Коллизий не найдено")
    # Решения уравнения совпадают, т.е. есть только одна точка
    elif -epsilon < disc < epsilon:
        t = -b/(2*a)
        x = d1[0]*t + line1[0]
        y = d1[1]*t + line1[1]
        z = d1[2]*t + line1[2]
        ans = [x, y, z]
        print(ans)
    # Есть 2 точки пересечения
    else:
        t1 = (-b + sqrt(disc) )/(2*a)
        t2 = (-b - sqrt(disc) )/(2*a)
        x = d1[0]*t1 + line1[0]
        y = d1[1]*t1 + line1[1]
        z = d1[2]*t1 + line1[2]
        ans = [x, y, z]
        print(ans, "\n")
        x = d1[0]*t2 + line1[0]
        y = d1[1]*t2 + line1[1]
        z = d1[2]*t2 + line1[2]
        ans = [x, y, z]
        print(ans)


# Получаем путь к файлу с данными из командной строки
path = "".join(sys.argv[1:])

string = []
with open(r"{}".format(path), "r") as file:
    for line in file:
        string.append(line)

string = " ".join(string)
list_data = string.split()


# Удаляем ненужные элементы
for i in range(len(list_data)):
    list_data[i] = list_data[i].replace("{", "")
    list_data[i] = list_data[i].replace("}", "")
    list_data[i] = list_data[i].replace("]", "")
    list_data[i] = list_data[i].replace("[", "")
    list_data[i] = list_data[i].replace(",", "")

# Сохраняем переменные
for i in range(len(list_data) - 1):
    if list_data[i] == "center:":
        centre = [float(list_data[i+1]), float(list_data[i+2]), float(list_data[i+3])]
    if list_data[i] == "radius:":
        R = float(list_data[i+1])
    if list_data[i] == "line:":
        line1 = [float(list_data[i+1]), float(list_data[i+2]), float(list_data[i+3])]
        line2 = [float(list_data[i+4]), float(list_data[i+5]), float(list_data[i+6])]



d1 = []
d2 = []
for i in range(len(line1)):
    d1.append(line2[i] - line1[i])
    d2.append(line1[i] - centre[i])

find_points(d1, d2, R, line1)



# Строим графики
fig = plt.figure()
ax = fig.add_subplot(111 , projection='3d')

# Строим сферу
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

xs = R * np.outer(np.cos(u), np.sin(v)) - centre[0]
ys = R * np.outer(np.sin(u), np.sin(v)) - centre[1]
zs = R * np.outer(np.ones(np.size(u)), np.cos(v)) - centre[2]
ax.plot_surface(xs, ys, zs,  rstride=4, cstride=4, color='b')

# Cтроим линию
t = np.linspace(-1, 1, 100)
x = d1[0]*t + line1[0]
y = d1[1]*t + line1[1]
z = d1[2]*t + line1[2]
ax.plot(x, y, z, color='r')

Axes3D.set_ylim(ax, [-R*1.2 - centre[1], R*1.2 + centre[1]])
Axes3D.set_xlim(ax, [-R*1.2 - centre[0], R*1.2 + centre[0]])
Axes3D.set_zlim(ax, [-R*1.2 - centre[2], R*1.2 + centre[2]])

plt.show()


