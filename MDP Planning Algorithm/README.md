#Markov Decision Process (MDP) Planning Algorithm:

The task is to implement an MDP planning algorithm and test the implementation on a simple example found in test.py.

The ChainMDP problem has been solved using the value iteration algorithm, that utilizes Bellman equations.
If there are 'n' possible states, then there are 'n' Bellman equations, one for each state. These 'n' equations contain 'n'
unknowns – the utilities of the states, whose solution can be obtained by solving them simultaneously.
The following pseudocode has been implemented in solver.py file.

a) Declare a policy array 'p' and a utility array 'u', defined for each state space 's', which is given to be      
's' = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, which is equal to the length of the state space and arbitrarily assign them to
zeros.

b) Iterate through each state in the state space and compute 'U(s)' for each state by using the Bellman equation.
The utility of each state is continuously updated using utility of its neighbors, till an equilibrium state is reached.
γ is the discount factor, which if kept close to zero reduces the influence of the contribution of utility from distant
factors.

c) Iterate through each state space and update policy array with actions that result in maximum utility value.
