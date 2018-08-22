class Solver:
    def __init__(self, mdp):
        self.mdp = mdp
        self.state_spaces = mdp.S()
        self.actions = mdp.A()
        self.policy = []
        self.gamma = mdp.gamma()

    def solve(self):
        self.policy = [0 for s in range(len(self.state_spaces))]
        U = self.policy[:]

        continue_loop = True
        while continue_loop:
            continue_loop = False
            for s in self.state_spaces:
                U[s] = sum([self.mdp.P(s, self.policy[s], s1) \
                            * (self.mdp.R(s) + self.gamma * U[s1]) for s1 in self.state_spaces])

            for s in self.state_spaces:
                max_val = U[s]
                for a in self.actions:
                    q1 = sum([self.mdp.P(s, a, s1) \
                              * (self.mdp.R(s) + self.gamma * U[s1]) for s1 in self.state_spaces])
                    if q1 > max_val:
                        self.policy[s] = a
                        max_val = q1
                        continue_loop = True

        return self.policy
    
