class Solver:
    def __init__(self, mdp):
        self.mdp = mdp
        self.state_spaces = mdp.finite_states()
        self.actions = mdp.finite_actions()
        self.policy = []
        self.gamma = mdp.gamma()

    def solve(self):
        self.policy = [0 for _ in range(len(self.state_spaces))]
        u = self.policy[:]

        continue_loop = True
        while continue_loop:
            continue_loop = False
            for s in self.state_spaces:
                u[s] = sum(
                    [
                        self.mdp.p(s, self.policy[s], s1) * (self.mdp.r(s) + self.gamma * u[s1])
                        for s1 in self.state_spaces
                    ]
                )

            for s in self.state_spaces:
                max_val = u[s]
                for a in self.actions:
                    q1 = sum(
                        [
                            self.mdp.p(s, a, s1) * (self.mdp.r(s) + self.gamma * u[s1])
                            for s1 in self.state_spaces
                        ]
                    )
                    if q1 > max_val:
                        self.policy[s] = a
                        max_val = q1
                        continue_loop = True

        return self.policy
