import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Ініціалізація лічильника для всіх можливих сум (від 2 до 12)
    sum_counts = {total: 0 for total in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    # Обрахування ймовірності випаду кожної суми
    probabilities = {total: count / num_rolls for total, count in sum_counts.items()}

    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    plt.bar(sums, probs, tick_label=sums, color='skyblue', edgecolor='black')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob + 0.001, f"{prob * 100:.2f}%", ha='center')

    plt.ylim(0, max(probs) + 0.05)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nРезультати для {accuracy} кидків:")
        probabilities = simulate_dice_rolls(accuracy)
        for total in sorted(probabilities.keys()):
            print(f"Сума {total}: {probabilities[total]*100:.2f}%")
        plot_probabilities(probabilities)
