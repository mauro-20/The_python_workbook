# Scrabble Score

def scrabble_score(word):
    word = word.upper()
    score = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
             4: ['F', 'H', 'V', 'W', 'Y'], 5: 'K', 8: ['J', 'X'], 10: ['Q', 'Z']}

    result = 0
    for c in word:
        for k in score:
            if c in score[k]:
                result += k

    return result


print(scrabble_score('prova'))
