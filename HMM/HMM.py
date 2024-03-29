import numpy as np
import matplotlib.pyplot as plt

# 0 is paper, 1 is rock, 2 is scissors
pattern = [0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 0, 0, 0, 1, 2, 0, 2]
opponent_moves = pattern * 10

transition_matrix = np.zeros((3, 3))

def update_transition_matrix(transition_matrix, last_move, opponent_move):
    transition_matrix[last_move, opponent_move] += 0.1
    transition_matrix[last_move] /= transition_matrix[last_move].sum()

def choose_move(transition_matrix, last_opponent_move):
    predicted_move = np.argmax(transition_matrix[last_opponent_move])
    if predicted_move == 0:
        return 2 
    elif predicted_move == 1: 
        return 0  
    else: 
        return 1

def get_game_result(our_move, opponent_move):
    if our_move == opponent_move:
        return 0  # draw
    elif our_move == 0 and opponent_move == 1:  # paper beats rock
        return 1
    elif our_move == 1 and opponent_move == 2:  # rock beats scissors
        return 1
    elif our_move == 2 and opponent_move == 0:  # scissors beats paper
        return 1
    else:
        return -1 # loss


print("Lets the game begin!")
cash = 0
cash_history = [cash]
last_opponent_move = None

for i, opponent_move in enumerate(opponent_moves):
    print()
    print("Iteration number", i + 1)
    print(transition_matrix)
    if last_opponent_move is None or i < 5:
        our_move = np.random.choice([0, 1, 2])
    else:
        our_move = choose_move(transition_matrix, last_opponent_move)

    if last_opponent_move is not None:
        update_transition_matrix(transition_matrix, last_opponent_move, opponent_move)

    print("Enemy move", opponent_move)
    print("My move", our_move)
    result = get_game_result(our_move, opponent_move)
    print("Result", result)
    cash += result
    cash_history.append(cash)

    last_opponent_move = opponent_move

plt.plot(cash_history)
plt.xlabel("Game Number")
plt.ylabel("Cash Balance")
plt.title("Change in Cash Balance in 'Rock, Paper, Scissors'")
plt.show()