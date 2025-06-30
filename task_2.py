import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Кінцева точка поточної гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], color='green', linewidth=depth)

    # Кут відхилення для гілок
    angle_left = angle + np.pi / 4
    angle_right = angle - np.pi / 4

    # Коротша довжина для наступного рівня
    new_length = length * 0.7

    # Рекурсивно малюємо ліву і праву гілку
    draw_branch(x_end, y_end, angle_left, new_length, depth - 1)
    draw_branch(x_end, y_end, angle_right, new_length, depth - 1)


# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

# Запит глибини у користувача
depth = int(input("Введіть рівень рекурсії (бажано до 15): "))

# Початкові параметри: координати, кут, довжина
draw_branch(x=0, y=0, angle=np.pi / 2, length=1, depth=depth)

plt.show()
