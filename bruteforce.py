from itertools import combinations


def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    actions = []
    for line in lines[1:]:
        data = line.strip().split("\t")
        if len(data) < 3:  
            print(f"Ligne mal formatée: {line}")
            continue
        action_name = data[0]
        cost = float(data[1])
        profit_percentage = float(data[2].replace('%', ''))
        actions.append((action_name, cost, profit_percentage))

    return actions

def brute_force(actions):
    best_profit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        for subset in combinations(actions, r):
            total_cost = sum(item[1] for item in subset)
            if total_cost <= 500:
                total_profit = sum(item[1] * (item[2] / 100) for item in subset)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = subset

    return best_combination, best_profit

def main():
    actions = read_file("actions.txt")
    best_combination, best_profit = brute_force(actions)

    print("Meilleure combinaison d'investissement:")
    for action in best_combination:
        print(f"{action[0]} - Coût: {action[1]}€ - Bénéfice après 2 ans: {action[2]}%")

    print(f"\nProfit total après 2 ans: {best_profit:.2f}€")

if __name__ == "__main__":
    main()



