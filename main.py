import random

def calculate_probability(k):
    probabilities = []
    for i in range(6, k+1):
        bob_wins = 0
        alice_wins = 0
        for _ in range(10000):
            while True:
                if random.randint(1, i) == i:
                    bob_wins += 1
                    break
                if random.randint(1, i) == i:
                    alice_wins += 1
                    break
        probabilities.append(bob_wins / (bob_wins + alice_wins))
    return probabilities

if __name__ == "__main__":
    probabilities = calculate_probability(99)
    print(probabilities)