import solver


class ChainMDP:

    @staticmethod
    def p(s, a, u):
        """
        Returns the probability of transitioning from state s to state u when taking action a
        :param s:
        :param a:
        :param u:
        :return:
        """

        if a == "left" and u == s - 1:
            return 0.7
        if a == "left" and u == s + 1:
            return 0.3
        if a == "left" and s == 0 and u == 0:
            return 0.7
        if a == "right" and u == s + 1:
            return 0.7
        if a == "right" and u == s - 1:
            return 0.3
        if a == "right" and u == s and u == 10:
            return 0.7
        return 0.0

    @staticmethod
    def gamma():
        """
        Returns the discount factor that you can assume is in (0,1).
        :return:
        """

        return 0.9

    @staticmethod
    def r(y):
        """
        Accepts a state and returns the reward for visiting that state
        :param y:
        :return:
        """

        if y == 0 or y == 10:
            return 1.0
        return 0.0

    @staticmethod
    def finite_actions():
        """
        Returns a finite set of actions, which you can assume will be hashable
        :return:
        """

        return ["left", "right"]

    @staticmethod
    def finite_states():
        """
        Returns a finite set of states, which you can assume will be hashable
        :return:
        """

        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @staticmethod
    def initial_state():
        return 5


mdp = ChainMDP()
solve = solver.Solver(mdp)
policy = solve.solve()

for i in range(0, 5):
    assert (policy[i] == "left")

for i in range(6, 11):
    assert (policy[i] == "right")
