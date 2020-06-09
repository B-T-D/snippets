import random

def maybe_do_something(probability):
    if random.random() < probability: # '<' operator because can return 0.0
                                        # but not 1.0
        print("Do something")
        return 1
    return 0

probability = 0.5 # float in [0.0, 1.0)
trials = 10

did = 0
for i in range(trials):
    did += maybe_do_something(probability)
print(f"Did something {did} times out of {trials}")
    
