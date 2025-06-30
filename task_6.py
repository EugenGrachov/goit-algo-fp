# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    # Сортуємо страви за спаданням калорійності за одиницю вартості
    sorted_items = sorted(items.items(), 
                          key=lambda x: x[1]['calories'] / x[1]['cost'], 
                          reverse=True)

    for item, details in sorted_items:
        cost = details['cost']
        calories = details['calories']
        # Вибираємо блюдо, якщо вистачає бюджету
        if cost <= remaining_budget:
            chosen_items.append(item)
            remaining_budget -= cost
            total_calories += calories

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # DP таблиця: dp[i][w] = макс калорії, використовуючи перші i страв, з бюджетом w
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        for w in range(budget + 1):
            if cost <= w:
                # Вибираємо максимум: взяти цю страву або ні
                dp_table[i][w] = max(
                    calories + dp_table[i - 1][w - cost],
                    dp_table[i - 1][w]
                )
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    # Відновлення вибраних страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            item = item_names[i - 1]
            chosen_items.append(item)
            w -= items[item]['cost']

    chosen_items.reverse()
    total_calories = dp_table[n][budget]
    spent = budget - w

    return total_calories, spent, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy:", greedy_result)
    print("Dynamic Programming:", dp_result)
