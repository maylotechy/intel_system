import random

# Configuration
TARGET = "GENETIC ALGORITHM"
GENES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
POPULATION_SIZE = 100
MUTATION_RATE = 0.01

def create_individual():
    """Create a random string of the same length as the target."""
    return "".join(random.choice(GENES) for _ in range(len(TARGET)))

def calculate_fitness(individual):
    """Score is the number of characters matching the target."""
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

def mutate(individual):
    """Randomly flip a character based on mutation rate."""
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(GENES)
    return "".join(individual)

def crossover(parent1, parent2):
    """Combine two parents at a random midpoint."""
    point = random.randint(0, len(TARGET) - 1)
    child = parent1[:point] + parent2[point:]
    return child

# Main Loop
population = [create_individual() for _ in range(POPULATION_SIZE)]
generation = 0
found = False

while not found:
    population.sort(key=calculate_fitness, reverse=True)
    best = population[0]
    
    if calculate_fitness(best) == len(TARGET):
        found = True
        break
        
    print(f"Gen {generation} | Best: {best} | Fitness: {calculate_fitness(best)}")
    
    # Create next generation
    new_gen = population[:10] # Elitism: Keep top 10
    while len(new_gen) < POPULATION_SIZE:
        p1, p2 = random.sample(population[:50], 2)
        child = mutate(crossover(p1, p2))
        new_gen.append(child)
    
    population = new_gen
    generation += 1

print(f"Success! Final String: {best} in {generation} generations.")
