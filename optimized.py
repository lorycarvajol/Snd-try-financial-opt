def knapsack(actions, budget):
    n = len(actions)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        action_name, cost, profit_percentage = actions[i-1]
        for w in range(budget + 1):
            if cost <= w:
                profit = int(cost * (profit_percentage / 100))
                dp[i][w] = max(dp[i-1][w], profit + dp[i-1][w-int(cost)])
            else:
                dp[i][w] = dp[i-1][w]
                
    
    # Extract the list of actions chosen
    chosen_actions = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_actions.append(actions[i-1])
            w -= int(actions[i-1][1])

    return dp[n][budget], chosen_actions


def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    actions = []
    for line in lines[1:]:
        data = line.strip().split("\t")
        if len(data) < 3:  # Vérifiez le nombre d'éléments
            print(f"Ligne mal formatée: {line}")
            continue
        action_name = data[0]
        cost = float(data[1])
        profit_percentage = float(data[2].replace('%', ''))
        actions.append((action_name, cost, profit_percentage))

    return actions



def main():
    actions = read_file("actions.txt")
    profit, best_combination = knapsack(actions, 500)

    print("Meilleure combinaison d'investissement:")
    for action in best_combination:
        print(
            f"{action[0]} - Coût: {action[1]}€ - Bénéfice après 2 ans: {action[2]}%")

    print(f"\nProfit total après 2 ans: {profit:.2f}€")


if __name__ == "__main__":
    main()
