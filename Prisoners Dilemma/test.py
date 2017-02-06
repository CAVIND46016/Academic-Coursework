import alice
import random

a = alice.Alice()
print(a.name())

N = 100

utility = 0

for i in range(N):
    action_alice = a.get_action()
    action_bob = "BETRAY" if random.random() < 0.5 else "SILENT"
    a.give_action(action_bob); #Updates bob's action to opponent history list.
    
    assert(action_alice in ["BETRAY", "SILENT"])
  
    if action_alice == "BETRAY" and action_bob == "BETRAY":
        utility -= 2
    if action_alice == "SILENT" and action_bob == "BETRAY":
        utility -= 3
    if action_alice == "BETRAY" and action_bob == "SILENT":
        utility -= 0
    if action_alice == "SILENT" and action_bob == "SILENT":
        utility -= 1

a.game_over()

print("utility was: " + str(utility))

