def get_combinations(items, len_combination):
    if len_combination == 0:
        yield []
    else:
        for i in range(len(items)):
            current_item = items[i]
            remaining = items[i + 1:]
            for comb in get_combinations(remaining, len_combination - 1):
                yield [current_item] + comb


def brute_force_knapsack(file_location):
    with open(file_location, 'r') as file:
        capacity, num_items = map(int, file.readline().split())
        values = list(map(int, file.readline().split(',')))
        weights = list(map(int, file.readline().split(',')))

    best_value = 0
    best_combination = []
    total_iterations = 0
    best_iteration_number = 0

    for r in range(1, num_items + 1):
        all_combinations = get_combinations(range(num_items), r)
        for combination in all_combinations:
            total_iterations += 1

            current_value = 0
            current_weight = 0

            for i in combination:
                current_value += values[i]
                current_weight += weights[i]

            if current_weight <= capacity and current_value > best_value:
                best_iteration_number = total_iterations
                print(combination)
                best_value = current_value
                best_combination = [0] * num_items
                for i in combination:
                    best_combination[i] = 1
                print("--------------FOUND BEST-----------------")
                print(f"Iteration: {total_iterations}")
                print(f"Best combination: {best_combination}")
                print(f"Best value: {best_value}")
                print("----------------------------------------")

            if total_iterations % 1000000 == 0:
                print(f"Iteration: {total_iterations}")
                print(f"Best combination: {best_combination}")
                print(f"Current combination: {combination}")
                print(f"Value of the combination: {current_value}")
                print(f"Best value: {best_value}")
                print("----------------------------------------")

    print(f"Total iterations: {total_iterations}")
    print(f"Number of best iteration: {best_iteration_number}")
    print(f"Best combination: {best_combination}")
    print(f"Best value: {best_value}")


brute_force_knapsack('knapsack.txt')
