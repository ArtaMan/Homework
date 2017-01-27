import amosov as player1
import Gusarov as player2

word2 = 'Москва'
while True:
    word1 = player1.game(word2)
    # print(word1)
    word2 = player2.game(word1)
    print(word1, word2)
    # time.sleep(1)