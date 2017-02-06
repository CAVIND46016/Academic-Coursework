import random

class Alice:
    opponentHistory = None;
    #The constructor for your class. Use this to initialise your player.
    def __init__(self):
        self.selfHistory        = [];
        self.opponentHistory    = [];
        #Lookup three previous opponents strategies
        self.strategy_lookup    = {'SILENT' : 'SILENT', 
                                   'BETRAY' : 'BETRAY'};
  
    #Returns the name of your player. It may be anything (non-offensive) that
    #you choose except \Alice", because that isn’t her real name. Will be public on the
    #scoreboard, so choose something with high entropy if you don’t want to be identified
    def name(self):
        return "DSOUZAC";

    #Returns the action, either \BETRAY" or \SILENT". You may choose this in any way you please.
    def get_action(self):
        if(len(self.opponentHistory) == 0):
            return "SILENT"; # Always co-operate on the first turn
        else:
            #***************************************************************************************
            #*    Title: Evolving strategies for an Iterated Prisoner's Dilemma tournament
            #*    Author: Martin Jones
            #*    Date: 04/12/2015
            #*    Availability: http://mojones.net/evolving-strategies-for-an-iterated-prisoners-dilemma-tournament.html
            #***************************************************************************************
            opponent_last_action = self.opponentHistory[-1];
            my_action = self.strategy_lookup[opponent_last_action]
            return my_action;

    #Gives you Bob’s action that you can use (if you wish) to refine
    #your decisions in the future. The value of action is a string, either \SILENT" or
    #\BETRAY"
    def give_action(self, action):
        self.opponentHistory.append(action);

    #This function will be called after the Nth interaction. The function need
    #not return anything, but may be useful if you want your agent to know when it is
    #playing a new game.
    def game_over(self):
        print("Game Over.")
