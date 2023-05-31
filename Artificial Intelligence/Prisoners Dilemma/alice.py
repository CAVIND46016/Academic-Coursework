class Alice:
    def __init__(self):
        """
        The constructor for your class. Use this to initialize your player.
        """

        self.self_history = []
        self.opponent_history = []

        # Lookup three previous opponents strategies
        self.strategy_lookup = {
            "SILENT": "SILENT",
            "BETRAY": "BETRAY"
        }

    @staticmethod
    def name():
        """
        Returns the name of your player. It may be anything non-offensive that
        you choose except "Alice", because that isn’t her real name. Will be public on the
        scoreboard, so choose something with high entropy if you don’t want to be identified
        :return:
        """

        return "DSOUZAC"

    def get_action(self):
        """
        Returns the action, either "BETRAY" or "SILENT". You may choose this in any way you please.
        :return:
        """

        if len(self.opponent_history) == 0:
            return "SILENT"  # Always co-operate on the first turn
        else:
            # ***************************************************************************************
            # * Title: Evolving strategies for an Iterated Prisoner's Dilemma tournament
            # * Author: Martin Jones
            # * Date: 04/12/2015
            # * Availability: http://mojones.net/evolving-strategies-for-an-iterated-prisoners-dilemma-tournament.html
            # ***************************************************************************************
            opponent_last_action = self.opponent_history[-1]
            my_action = self.strategy_lookup[opponent_last_action]
            return my_action

    def give_action(self, action):
        """
        Gives you Bob’s action that you can use (if you wish)
        to refine your decisions in the future. The value of
        action is a string, either "SILENT" or "BETRAY"
        :param action:
        :return:
        """

        self.opponent_history.append(action)

    @staticmethod
    def game_over():
        """
        This function will be called after the Nth interaction. The function need
        not return anything, but may be useful if you want your agent to know when it is
        playing a new game.
        :return:
        """

        print("Game Over.")
