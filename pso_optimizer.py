import random

class Particle:
    def __init__(self):
        self.position = random.uniform(-10, 10)
        self.velocity = random.uniform(-1, 1)
        self.pbest_pos = self.position
        self.pbest_val = self.position ** 2

def pso_search(iterations=50):
    swarm = [Particle() for _ in range(20)]
    gbest_pos = swarm[0].position
    gbest_val = gbest_pos ** 2
    
    w, c1, c2 = 0.5, 1.5, 1.5 # Inertia and acceleration constants
    
    for i in range(iterations):
        for p in swarm:
            current_val = p.position ** 2
            
            # Update Personal Best
            if current_val < p.pbest_val:
                p.pbest_val = current_val
                p.pbest_pos = p.position
            
            # Update Global Best
            if current_val < gbest_val:
                gbest_val = current_val
                gbest_pos = p.position
                
        # Move Particles
        for p in swarm:
            r1, r2 = random.random(), random.random()
            p.velocity = (w * p.velocity) + \
                         (c1 * r1 * (p.pbest_pos - p.position)) + \
                         (c2 * r2 * (gbest_pos - p.position))
            p.position += p.velocity
            
        print(f"Iteration {i}: Global Best Value = {gbest_val:.6f} at x = {gbest_pos:.6f}")

if __name__ == "__main__":
    pso_search()
