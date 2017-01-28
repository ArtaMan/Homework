import game_amosov as player1

while True:
    word1 = input('введите слово ')
    word2 = player1.game(word1)
    print(word1, word2)