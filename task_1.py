import random
import math


def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(*bound) for bound in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        neighbor = [xi + random.uniform(-epsilon, epsilon) for xi in current_solution]
        neighbor = [
            max(min(neighbor[i], bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]

        neighbor_value = func(neighbor)
        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

        if abs(current_value) < epsilon:
            break

    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(*bound) for bound in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(*bound) for bound in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if abs(best_value) < epsilon:
            break

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current_solution = [random.uniform(*bound) for bound in bounds]
    current_value = func(current_solution)

    for i in range(iterations):
        new_solution = [
            xi + random.uniform(-epsilon, epsilon) for xi in current_solution
        ]
        new_solution = [
            max(min(new_solution[i], bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]

        new_value = func(new_solution)
        delta = new_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution, current_value = new_solution, new_value

        temp *= cooling_rate
        if temp < epsilon:
            break

    return current_solution, current_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
