import numpy as np

# States: 0=Charging, 1=Exploring, 2=Stuck
states = ["Charging", "Exploring", "Stuck"]

# Transition Probability Matrix (P)
# Rows = current state, Columns = next state
# e.g., If Exploring (Row 1), there is a 10% chance of getting Stuck (Col 2)
P = np.array([
    [0.7, 0.3, 0.0], # Charging
    [0.2, 0.7, 0.1], # Exploring
    [0.5, 0.0, 0.5]  # Stuck
])

def simulate_mdp(steps=10):
    current_state = 0 # Start at Charging
    print(f"Starting State: {states[current_state]}")
    
    for i in range(1, steps + 1):
        # Choose next state based on probabilities of current state row
        next_state = np.random.choice([0, 1, 2], p=P[current_state])
        print(f"Step {i}: Moved to {states[next_state]}")
        current_state = next_state

if __name__ == "__main__":
    simulate_mdp()
