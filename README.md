
Computational Intelligence & Decision Models
​This repository explores three fundamental paradigms in modern AI and optimization: Genetic Algorithms (GA), Particle Swarm Optimization (PSO), and Markov Decision Processes (MDP). Each section below provides a detailed description, the logic behind the algorithm, and two real-world application examples.
​1. Genetic Algorithm (GA)
​Description
​The Genetic Algorithm is a metaheuristic inspired by the process of natural selection and belongs to the larger class of evolutionary algorithms (EA). It is designed to solve optimization problems by mimicking the "survival of the fittest" principle.
​A population of candidate solutions (called individuals or chromosomes) is evolved toward better solutions. Each individual has a set of properties which can be mutated and altered. The evolution usually starts from a population of randomly generated individuals and is an iterative process, with the population in each iteration called a generation.
​Core Components
​Fitness Function: Quantifies how "good" a solution is.
​Selection: Retains the best individuals to pass their "genes" to the next generation.
​Crossover (Recombination): Combines parts of two parents to create offspring.
​Mutation: Introduces random changes to maintain diversity and prevent premature convergence.
​Examples
​The Traveling Salesman Problem (TSP): In logistics, finding the most efficient route for a vehicle to visit multiple locations and return home. GA evolves various route sequences, "breeding" shorter paths together to eventually find the global or near-global minimum distance.
​Antenna Design: NASA has used GAs to evolve the shapes of antennas for spacecraft. By simulating electromagnetic performance as "fitness," the algorithm "grows" complex, non-intuitive shapes that outperform traditional human-designed antennas.
​2. Particle Swarm Optimization (PSO)
​Description
​Particle Swarm Optimization is a social-behavior-based optimization technique. Unlike Genetic Algorithms, which rely on competition and elimination, PSO relies on cooperation. It was originally intended for simulating social behavior, such as the choreographed motion of a flock of birds or a school of fish.
​In PSO, each "particle" (candidate solution) flies through a multi-dimensional search space. Each particle keeps track of its own best-achieved position (pbest) and the best position achieved by any particle in the entire swarm (gbest). Particles adjust their velocity based on these two points, effectively "pulling" the swarm toward the most promising areas of the search space.
​Core Components
​Velocity: The direction and speed at which a particle moves.
​Inertia: The tendency of a particle to continue in its current direction.
​Cognitive Component: The particle’s memory of its own best performance.
​Social Component: The swarm’s collective knowledge of the best performance.
​Examples
​Neural Network Training: PSO can be used to optimize the weights and biases of an Artificial Neural Network. This is particularly useful in "Black Box" optimization where gradient-based methods (like Backpropagation) might get stuck in local minima.
​Hydrothermal Scheduling: Power companies use PSO to determine the optimal hourly generation schedule for a mix of hydroelectric and thermal power plants to meet electricity demand at the lowest possible cost while respecting dam water levels.
​3. Markov Decision Process (MDP)
​Description
​A Markov Decision Process provides a mathematical framework for modeling decision-making in situations where outcomes are partly random and partly under the control of a decision-maker. It is the core mathematical foundation for Reinforcement Learning (RL).
​The fundamental assumption of an MDP is the Markov Property: the future depends only on the current state and action, not on the sequence of events that preceded it. The goal of an MDP is to find a "policy" (\pi)—a mapping of states to actions—that maximizes the total cumulative reward over time.
​Core Components
​States (S): A set of all possible environmental configurations.
​Actions (A): The set of choices available to the agent.
​Transition Probability (P): The likelihood that action a in state s will lead to state s'.
​Reward (R): The immediate feedback (positive or negative) received after a transition.
​Examples
​Autonomous Vehicle Navigation: A self-driving car must decide whether to accelerate, brake, or steer (Actions) based on its current position and surrounding traffic (States). Since traffic and weather are unpredictable, the transitions are stochastic (probabilistic), and the "Reward" is reaching the destination safely and efficiently.
​Personalized Medicine: MDPs are used to determine optimal treatment plans for chronic diseases. The patient’s health indicators are the "States," different medications/dosages are "Actions," and the "Reward" is a measurement of the patient’s long-term recovery or quality of life.
