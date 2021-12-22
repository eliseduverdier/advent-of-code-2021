# ===== SAMPLE
# player1pos = 4 - 1
# player2pos = 8 - 1
# ===== INPUT
player1pos = 4 - 1
player2pos = 6 - 1

board = range(0, 10) # easier, will add 1 to every score later

# ========================= STEP 1 ================================
def play(player1pos, player2pos):
    player1score = 0
    player2score = 0
    step = 0
    FINAL_SCORE = 1000
    while player1score < FINAL_SCORE and player2score < FINAL_SCORE:
        dice = 9*step + 6 # thanks oeis

        if step % 2 == 0: # if step is even, player 1 plays, otherwise player 2
            player1pos = board[ (player1pos + dice) % 10 ]
            player1score += player1pos+1
        else:
            player2pos = board[ (player2pos + dice) % 10 ]
            player2score += player2pos+1
        step += 1

    print(f'player1score: {player1score}, player2score: {player2score}, 🎲️: {dice}, step*3: {step*3}')
    print('Result:', min(player1score, player2score) * step*3)

# play(player1pos, player2pos)
# ========================= STEP 2 ================================

scoreCache = {}
def quantumPlay(player1pos, player2pos, player1score, player2score, step = 0):
    # print('  '*step, f'🎲️ PLAYER1 score {player1score}, pos {player1pos} / PLAYER2 score {player2score}, pos {player2pos}')
    FINAL_SCORE = 21 # or
    if player1score >= FINAL_SCORE:
        return (1, 0)
    elif player2score >= FINAL_SCORE:
        return (0, 1)
    elif (player1pos, player2pos, player1score, player2score) in scoreCache:
        return scoreCache[(player1pos, player2pos, player1score, player2score)]
    else:
        result = (0,0)
        for die1 in range(1,4): # split universes
            for die2 in range(1,4): # again!
                for die3 in range(1,4): # agaaain!
                    newPlayer1pos = (player1pos + die1 + die2 + die3) % 10
                    newPlayer1score = player1score + newPlayer1pos + 1
                    winning1, winning2 = quantumPlay(player2pos, newPlayer1pos, player2score, newPlayer1score, step+1)
                    result = (result[0]+winning2, result[1]+winning1)
        scoreCache[(player1pos, player2pos, player1score, player2score)] = result # store for next calls
        return result

game = quantumPlay(player1pos, player2pos, 0, 0)
print(game, max(game))

